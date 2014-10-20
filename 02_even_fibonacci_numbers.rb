LIMIT = 4000000

def main
  arr = []
  a = b = 1
  while(a < LIMIT) do
    arr << a
    a, b = b, a + b
  end
  arr.select { |x| x % 2 == 0 }
  puts arr.inject(0, :+)
end

main
