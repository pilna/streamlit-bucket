from threading import Lock


class SingletonMeta(type):
    """
    It's a metaclass that creates a singleton class.
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        """
        If the class has not been instantiated, instantiate it and store it in a dictionary. 
        If the class has been instantiated, return the instance stored in the dictionary
        
        Parameters:
            cls
                The class that is being decorated.
        
        Returns:
            The instance of the class.
        """
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]