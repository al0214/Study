public class One {
    public static void main(String[] args) {
        int a,b;
        a = 10;
        b = ++a + 10;
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        a = 10;
        b = a++ + 10;
        System.out.println("a = " + a);
        System.out.println("a = " + b);
        a = 10;
        b = --a + 10;
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        a = 10;
        b = a-- + 10;
        System.out.println("a = " + a);
        System.out.println("a = " + b);

    }
}
