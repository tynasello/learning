package decorator_pattern;

public class Margherita extends Pizza {
    public Margherita() {
        description = "Margherita pizza";
    }

    @Override
    public double cost() {
        return 8.50;
    }
}
