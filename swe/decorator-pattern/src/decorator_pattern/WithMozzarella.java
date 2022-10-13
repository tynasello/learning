package decorator_pattern;

public class WithMozzarella extends PizzaDecorator {
    Pizza pizza;
    double mozzarellaCost = .55;

    public WithMozzarella(Pizza pizza) {
        this.pizza = pizza;
        this.description = pizza.description + ", mozzarella";

    }

    @Override
    public double cost() {
        return pizza.cost() + mozzarellaCost;
    }
}
