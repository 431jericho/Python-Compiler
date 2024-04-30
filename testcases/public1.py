class A:

  def __init__(self: A, a: int, b: int, c: int) -> None:
    self.x: int = a
    self.y: int = b
    print(self.x * self.y)

  def print_name(self: A, a: int) -> None:
    print(self.x * self.y)

def main() -> None:  
  o: A = A(3, 4, 5)
  o.print_name(3)

if __name__ == "__main__":
    main()
