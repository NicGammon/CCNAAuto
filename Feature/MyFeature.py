class MyFeature:
    """A basic feature class."""
    
    def __init__(self):
        """Initialize the feature."""
        self.enabled = True
    
    def execute(self):
        """Execute the feature."""
        if self.enabled:
            print("Feature is executing")
            return True
        return False
    
    def disable(self):
        """Disable the feature."""
        self.enabled = False
    
    def enable(self):
        """Enable the feature."""
        self.enabled = True


if __name__ == "__main__":
    feature = MyFeature()
    feature.execute()