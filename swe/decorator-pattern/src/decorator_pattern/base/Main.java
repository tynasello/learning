package decorator_pattern.base;

import decorator_pattern.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Pizza margherita = new Margherita();
        System.out.println(margherita.getDescription() + ", " + margherita.cost());

        margherita = new WithTomato(margherita);
        System.out.println(margherita.getDescription() + " (" + margherita.cost() + ")");

        margherita = new WithMozzarella(margherita);
        margherita = new WithBasil(margherita);
        System.out.println(margherita.getDescription() + " (" + margherita.cost() + ")");
    }
}
