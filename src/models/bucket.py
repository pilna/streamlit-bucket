
class Bucket:
    """
    A class that represent a bucket.

    Attributes:
        bucket_name: str
            the name of the bucket (preferable that it be unique)
        max_volume: int
            The maximum volume of the bucket.
        current_volume: int
            The current volume are store in the bucket.

    Methods:
        receive_volume(bucket: Bucket)
            Receive the volume of a bucket and store it in the current volume of the bucket

        drain_volume()
            Drain the volume of the Bucket.

        fill_the_volume()
            Fill the volume of the bucket to its maximum volume.
            
        pour_the_volume_in(bucket: Bucket)
            The function is used to pour the volume of the bucket into the other bucket.
    """

    def __init__(self, bucket_name: str, max_volume: int, current_volume: int = 0) -> None:
        """
        Parameters: 
            bucket_name: str
                the name of the bucket (preferable that it be unique)
            max_volume: int
                The maximum volume of the bucket.
            current_volume: int (optional)
                The current volume of the bucket
        """
        self.name = bucket_name
        self.max_volume = max_volume
        self.current_volume = current_volume


    def receive_volume(self, bucket: 'Bucket') -> int:
        """
        Receive the volume of a bucket and store it in the current volume of the bucket
        
        Parameters:
            bucket: Bucket
        
        Return: int
            The amount of water that cannot be stored in the bucket.
        """
        new_volume = self.current_volume + bucket.current_volume
        self.current_volume = min(new_volume, self.max_volume)
        return new_volume - self.max_volume if self.max_volume < new_volume else 0


    def drain(self) -> None:
        """
        Drain the volume of the Bucket.
        """
        self.current_volume = 0


    def fill(self) -> None:
        """
        Fill the volume of the bucket to its maximum volume.
        """
        self.current_volume = self.max_volume


    def pour_volume_in(self, bucket: 'Bucket') -> None:
        """
        The function is used to pour the volume of the bucket into the other bucket.
        
        Parameters:
            bucket: Bucket
                the bucket in which you want to pour your volume.
        """
        if not isinstance(bucket, Bucket):
            raise TypeError(f"the bucket type is expected but type {type(bucket)} is given")
        self.current_volume = bucket.receive_volume(self)


    def __eq__(self, bucket: 'Bucket') -> bool:
        """
        The function is used to compare two Bucket objects.
        
        Parameter:
            bucket: Bucket
                the bucket you want to compare.
        """
        if not isinstance(bucket, Bucket):
            raise TypeError(f"the bucket type is expected but type {type(bucket)} is given")
        return (
            self.max_volume == bucket.max_volume 
            and self.current_volume == bucket.current_volume
            and self.name == bucket.name
        )


    def __hash__(self) -> int:
        """
        The __hash__ method is called when we try to convert an object to a hash value. 
        In this case, we want to make sure that when we create a Stock object, 
        the hash value is based on the current_volume and max_volume attributes
        
        Return: 
            The hash value of the tuple (self.current_volume, self.max_volume).
        """
        return hash((self.current_volume, self.max_volume))
    

    def clone(self):
        """
        Create a new bucket with the same name, same max_volume and current_volume as the current bucket.

        Return: Bucket
            A new Bucket object with the same name, same max_volume and current_volume as the calling object.
        """
        return Bucket(self.name, self.max_volume, current_volume=self.current_volume)


    def __str__(self) -> str:
        """
        The function is used to cast the object in string

        Return: str
            a string that represents the bucket object.
        """
        return f"volume: {self.current_volume} / {self.max_volume}"
