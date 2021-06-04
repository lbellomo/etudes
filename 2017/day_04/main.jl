import StatsBase: countmap

function solve_a(data)
    count = 0

    for line in data
        if length(Set(line)) == length(line)
            count += 1
        end
    end
    count
end

function solve_b(data)
    count = 0

    for line in data
        if length(Set(countmap.(line))) == length(line)
            count += 1
        end
    end
    count
end

data = split.(readlines("input.txt"))

sol_a = solve_a(data)
println("sol a: $(sol_a)")

sol_b = solve_b(data)
println("sol b: $(sol_b)")