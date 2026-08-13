
class Solution:

    
    def checkPrime(self, n):
      
        cnt = 0

        
        for i in range(1, int(n**0.5) + 1):
        
            if n % i == 0:
         
                cnt += 1

                
                if n // i != i:
                    cnt += 1

        
        return cnt == 2

    # Function to return prime factors
    def getPrimeFactors(self, n):
        # List to store prime factors
        primeFactors = []

        # Loop from 2 to n
        for i in range(2, n + 1):
            # If divisible
            if n % i == 0:
                # Check if i is prime
                if self.checkPrime(i):
                    # Add to result
                    primeFactors.append(i)

        return primeFactors


# Driver code
if __name__ == "__main__":
    n = 60

   
    sol = Solution()

   
    ans = sol.getPrimeFactors(n)

   
    print(f"Prime Factors for {n}:", *ans)
