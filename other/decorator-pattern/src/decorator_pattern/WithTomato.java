package decorator_pattern;

public class WithTomato extends PizzaDecorator {
    Pizza pizza;
    double tomatoSauceCost = .20;
    double tomatoCost = .25;

    public WithTomato(Pizza pizza) {
        this.pizza = pizza;
        this.description = pizza.description + ", tomato";
    }

    @Override
    public double cost() {
        return pizza.cost() + tomatoSauceCost + tomatoCost;
    }
}
