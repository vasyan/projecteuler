def main
  arr = (1..1000).select { |x| x % 3 == 0 || x % 5 == 0 }
  puts arr.inject(0, :+)
end

main
