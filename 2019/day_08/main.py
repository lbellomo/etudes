from collections import Counter


def read_data(path_data: str) -> str:
    with open(path_data) as f_in:
        return f_in.read().strip()


def build_layers(data: str, wide: int, tall: int) -> list[str]:
    layer_len = wide * tall
    number_layers = len(data) // (layer_len)
    layers = [data[i * layer_len : (i + 1) * layer_len] for i in range(number_layers)]
    return layers


def solve_a(data: str, wide: int, tall: int) -> int:
    layers = build_layers(data, wide, tall)
    count_layers = [Counter(layer) for layer in layers]
    layer_min_zeros = min(count_layers, key=lambda x: x["0"])
    return layer_min_zeros["2"] * layer_min_zeros["1"]


def find_pixel(i: int, layers: list[str]) -> str:
    for layer in layers:
        pixel = layer[i]
        if pixel != "2":
            break
    return pixel


def solve_b(data: str, wide: int, tall: int) -> str:
    layers = build_layers(data, wide, tall)
    img = "".join(find_pixel(i, layers) for i in range(wide * tall))
    img = img.replace("0", " ")
    return img


if __name__ == "__main__":
    wide = 25
    tall = 6
    data = read_data("input.txt")
    sol_a = solve_a(data, wide, tall)
    print(f"sol a = {sol_a}")
    sol_b = solve_b(data, wide, tall)
    print("sol b = ")
    for i in range(tall):
        print(sol_b[i * wide : (i + 1) * wide])


def test_build_layers():
    data = "123456789012"
    layers = build_layers(data, 3, 2)
    assert layers == ["123456", "789012"]


def test_solve_b():
    data = "0222112222120000"
    img = solve_b(data, 2, 2)
    assert img == " 11 "
