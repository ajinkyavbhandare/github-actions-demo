from locust import HttpUser, between, task


class FastAPILoadTester(HttpUser):
    # Simulate a user waiting between 0.1 and 0.5 seconds between tasks
    wait_time = between(0.1, 0.5)

    @task(3)
    def test_root(self):
        """Test the root endpoint."""
        self.client.get("/")

    @task(1)
    def test_compute(self):
        """Test your compute endpoint."""
        # Adjust 'n' based on your experimental complexity
        payload = {"n": 1000}
        self.client.post("/compute", json=payload)
