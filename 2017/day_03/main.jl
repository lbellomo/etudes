function solve_a(target)
    pos = [0, 0]
    value = 1
    step_size = 0
    direction = -1
    
    while true
        step_size += 1
        direction *= -1
        for pos_index = 1:2
            for _ = 1:step_size
                pos[pos_index] += direction
                # println("pos: $(pos)")
                value += 1
                if value == target
                    # println(step_size)
                    return sum(abs.(pos))
                end
            end
        end
    end
end
    
function ∑neighbours(target_pos, know_pos)
    value = 0
    for i = -1:1, j = -1:1
        pos = target_pos + [i, j]
        value += get(know_pos, pos, 0)
    end
    value
end
    
function solve_b(target)
    pos = [0, 0]
    know_pos = Dict()
    know_pos[[0, 0]] = 1
    # value = 1
    step_size = 0
    direction = -1
    
    while true
        step_size += 1
        direction *= -1
        for pos_index = 1:2
            for _ = 1:step_size
                pos[pos_index] += direction
                value = ∑neighbours(pos, know_pos)
                know_pos[copy(pos)] = value
                # println(know_pos)
                if value >= target
                    # println(step_size)
                    return value
                end
            end
        end
    end
end


target = 368078

sol_a = solve_a(target)
println("sol a: $(sol_a)")

sol_b = solve_b(target)
println("sol b: $(sol_b)")