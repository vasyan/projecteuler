def main
  puts (1..1000).inject { |sum, x| sum += x ** x }.to_s[-10, 10].to_i
end

main
