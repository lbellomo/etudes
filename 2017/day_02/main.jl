using Combinatorics

function parsedata(raw_data)
    data = []
    for line in raw_data
        line = split(line, "\t")
        line = parse.(Int, line)
        push!(data, line)
    end
    data
end

function solve_a(data)
    total = 0

    for line in data
        total += maximum(line) - minimum(line)
    end
    total
end

function solve_b(data)
    total = 0
    for line in data
        for (i, j) in permutations(line,2)
            if i % j == 0
                total += i ÷ j
            end
        end
    end
    total
end

raw_data = readlines("input.txt")
data = parsedata(raw_data)
sol_a = solve_a(data)
println("sol a: $(sol_a)")

sol_b = solve_b(data)
println("sol b: $(sol_b)")