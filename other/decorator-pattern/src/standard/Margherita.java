package standard;

public class Margherita extends Pizza {
    public Margherita() {
        this.description = "Margherita Pizza";
        this.cost = 8.50;
        this.addTopping("tomato");
        this.addTopping("mozzarella");
        this.addTopping("basil");
    }

}
