with open("input.txt") as f:
    raw_data = [line.strip() for line in f]


total_time = 2503


class Reindeer:
    def __init__(self, name, speed, fly_duration, rest_duration):
        self.name = name
        self.speed = int(speed)
        self.fly_duration = int(fly_duration)
        self.rest_duration = int(rest_duration)

        self.distance = 0
        self.flying = True
        self.time_left = self.fly_duration

        self.score = 0

    def tick(self):
        # print(self.name, self.time_left, self.distance, self.state)

        self.time_left -= 1

        if self.flying:
            self.distance += self.speed

        if self.time_left == 0:
            if self.flying:
                self.time_left = self.rest_duration
            else:
                self.time_left = self.fly_duration
            self.flying = not self.flying

    def check_score(self, max_distance):
        if self.distance == max_distance:
            self.score += 1


def create_deers(raw_data):
    deers = []

    for line in raw_data:
        name, _, _, speed, _, _, fly_duration, *_, rest_duration, _ = line.split()
        deers.append(Reindeer(name, speed, fly_duration, rest_duration))

    return deers


def race(deers):
    for _ in range(total_time):
        for deer in deers:
            deer.tick()

        max_distance = max([deer.distance for deer in deers])
        for deer in deers:
            deer.check_score(max_distance)


deers = create_deers(raw_data)
race(deers)

sol_a = max([deer.distance for deer in deers])
print(f"{sol_a = }")
sol_b = max([deer.score for deer in deers])
print(f"{sol_b = }")
