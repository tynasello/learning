class Phone(notificationManager: NotificationManager) : Observer {
    
    init {
        notificationManager.registerObserver(this)
    }

    override fun update(notification: String) {
        println("-- User receiving notification -- $notification")
    }
}