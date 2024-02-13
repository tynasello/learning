class NotificationManager: Subject {
    var observers = mutableListOf<Observer>()
    
    override fun registerObserver(observer:Observer){
        this.observers.add(observer)
    }
    
    override fun notifyObservers(notification:String){
        for(observer in observers){
            observer.update(notification)
        }
    }
}