function solve_a(data::String)::Int
	total = 0
	len_data = length(data)
	
	for i = 1:len_data
		if i != len_data
			target_index = i+1
		else
			target_index = 1
		end
		
		if data[i] == data[target_index]
			total += parse(Int, data[i])
		 end
	end
	
	total
end

function solve_b(data::String)::Int
	total = 0
	len_data = length(data)
	half_len = len_data ÷ 2
	
	for i = 1:len_data
		target_index = i + half_len
		if target_index > len_data
			target_index %= len_data
		end
		
		if data[i] == data[target_index]
			total += parse(Int, data[i])
		end
	end
	
	total
end	

data = readline("input.txt")
sol_a = solve_a(data)
sol_b = solve_b(data)

println("sol a: $(sol_a)")
println("sol b: $(sol_b)")