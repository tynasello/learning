package standard.base;

import standard.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Pizza margherita = new Margherita();
        System.out.println(margherita.getDescription() + ", " + margherita.getCost());

    }
}
