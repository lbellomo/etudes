function reallocation!(state)
    len = length(state)
    index = argmax(state)
    value = state[index]
    state[index] = 0
    for i in 1:value
        target_index = index + i
        if target_index > len
            target_index = target_index % len
        end
        state[target_index] += 1
    end
end

function solve(state)
    # part a
    count = 1
    know_states = Set([copy(state)])

    while true
        reallocation!(state)
        if state ∈ know_states
            break
        end
        push!(know_states, copy(state))
        count += 1
    end
    sol_a = count
    # part b
    count = 1
    target_state = copy(state)
    while true
        reallocation!(state)
        if state == target_state
            break
        end
        count += 1
    end

    sol_b = count
    sol_a, sol_b
end

data = parse.(Int, split(readline("input.txt")));
sol_a, sol_b = solve(data)
println("sol a: $(sol_a)")
println("sol b: $(sol_b)")