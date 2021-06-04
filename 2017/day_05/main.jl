function solve_a(instructions)
    steps = 0

    index = 1
    len = length(instructions)
    while index < len + 1
        # println("before: $(index)")
        offset = instructions[index]
        instructions[index] += 1
        index += offset
        steps += 1
        # println("after: $(index), $(offset), ")
    end
    steps
end

function solve_b(instructions)
    steps = 0

    index = 1
    len = length(instructions)
    while index < len + 1
        # println("before: $(index)")
        offset = instructions[index]
        
        if offset >= 3
            instructions[index] -= 1
        else
            instructions[index] += 1
        end
        
        index += offset
        steps += 1
        # println("after: $(index), $(offset), ")
    end
    steps
end

data = parse.(Int, readlines("input.txt"));
sol_a = solve_a(copy(data))
println("sol a: $(sol_a)")

sol_b = solve_b(copy(data))
println("sol b: $(sol_b)")