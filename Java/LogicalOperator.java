public class LogicalOperator {
    public static void main(String[] args) {
        System.out.println('a' > 'b'); //False
        System.out.println(3 >= 2); // True
        System.out.println(-1 < 0); // True
        System.out.println(3.45 <= 2); // False
        System.out.println(3 == 2); // False
        System.out.println(3 != 2); // True
        System.out.println(!(3 != 2)); // False
        System.out.println((3 > 2) && (3 > 4)); // False
        System.out.println((3 != 2) || (-1 > 0)); // True
        System.out.println((3 != 2) ^ (-1 > 0)); // True
    }
}
