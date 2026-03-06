"""
Property Insurance Management System - Main Program
Student: Bishesh
Integration test showing all classes working together
"""


class Customer:
    """Parent class for managing insurance customers"""
    
    def __init__(self, customer_id, name, age, email):
        """Initialize a customer with basic information"""
        self._customer_id = None
        self._name = None
        self._age = None
        self._email = None
        
        # Set values using setters for validation
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.email = email

    # Getter and Setter for customer_id
    @property
    def customer_id(self):
        """Get customer ID"""
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        """
        Set customer ID with validation
        - Must be string
        - Length between 2 and 10 characters
        - Must start with C and remaining characters must be digits
        """
        if not isinstance(value, str):
            raise TypeError("Customer ID must be a string")

        if len(value) < 2 or len(value) > 10:
            raise ValueError("Customer ID length must be between 2 and 10 characters")

        if not value.startswith("C") or not value[1:].isdigit():
            raise ValueError("Customer ID must start with 'C' followed by digits (e.g., C001)")

        self._customer_id = value
    
    # Getter and Setter for name
    @property
    def name(self):
        """Get customer name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Set customer name with validation
        - Must be string
        - Length between 3 and 50 characters
        - Only alphabets and spaces allowed
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        if len(value) < 3 or len(value) > 50:
            raise ValueError("Name length must be between 3 and 50 characters")
        
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("Name can only contain letters and spaces")
        
        self._name = value

    # Getter and Setter for age
    @property
    def age(self):
        """Get customer age"""
        return self._age

    @age.setter
    def age(self, value):
        """
        Set customer age with validation
        - Must be a number
        - Must be whole number
        - Range between 18 and 100
        """
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")

        if value < 18 or value > 100:
            raise ValueError("Age must be between 18 and 100")

        self._age = value
    
    # Getter and Setter for email
    @property
    def email(self):
        """Get customer email"""
        return self._email
    
    @email.setter
    def email(self, value):
        """
        Set customer email with validation
        - Must be string
        - Must have @ symbol
        - Must have domain with dot
        """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        
        if '@' not in value:
            raise ValueError("Email must contain @")
        
        if '.' not in value:
            raise ValueError("Email must contain domain extension")
        
        parts = value.split('@')
        if len(parts) != 2:
            raise ValueError("Email format is invalid")
        
        self._email = value
    
    # Calculation and processing functions
    def calculate_insurance_cost(self, property_value):
        """Calculate insurance cost based on property value"""
        if not isinstance(property_value, (int, float)):
            raise TypeError("Property value must be a number")
        
        if property_value <= 0:
            raise ValueError("Property value must be greater than 0")
        
        # Base premium is 0.5% of property value
        premium = property_value * 0.005
        return premium
    
    def apply_discount(self, base_amount, discount_percent):
        """Apply discount to insurance amount"""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        
        discount_amount = base_amount * (discount_percent / 100)
        final_amount = base_amount - discount_amount
        return final_amount
    
    # Method to be overridden in child class
    def get_details(self):
        """Return customer information - can be overridden in child classes"""
        info = {
            "customer_id": self._customer_id,
            "name": self._name,
            "age": self._age,
            "email": self._email
        }
        return info
    
    # String representation
    def __str__(self):
        """Return string representation of customer"""
        return f"Customer: {self._name}, Age: {self._age}"


class PremiumCustomer(Customer):
    """Child class demonstrating method overriding from Customer"""

    def __init__(self, customer_id, name, age, email, loyalty_points):
        super().__init__(customer_id, name, age, email)
        self._loyalty_points = None
        self.loyalty_points = loyalty_points

    @property
    def loyalty_points(self):
        """Get loyalty points"""
        return self._loyalty_points

    @loyalty_points.setter
    def loyalty_points(self, value):
        """
        Set loyalty points with validation
        - Must be an integer
        - Range between 0 and 10000
        """
        if not isinstance(value, int):
            raise TypeError("Loyalty points must be an integer")

        if value < 0 or value > 10000:
            raise ValueError("Loyalty points must be between 0 and 10000")

        self._loyalty_points = value

    def get_details(self):
        """Override parent method and add premium customer details"""
        info = super().get_details()
        info["customer_type"] = "Premium"
        info["loyalty_points"] = self._loyalty_points
        return info


def run_customer_tests():
    """Run Customer and PremiumCustomer test cases"""
    print("="*70)
    print("Customer Class Testing")
    print("="*70)
    print()

    # Test 1: Create valid customer
    print("Test 1: Creating valid customer")
    try:
        customer1 = Customer("C001", "Bishesh Kumar", 23, "bishesh@email.com")
        print(f"Success: {customer1}")
        print(f"Email: {customer1.email}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 2: Create another customer
    print("Test 2: Creating another customer")
    try:
        customer2 = Customer("C002", "Priya Sharma", 29, "priya@email.com")
        print(f"Success: {customer2}")
        premium = customer2.calculate_insurance_cost(750000)
        print(f"Insurance Cost for 750000: ${premium:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 3: Using property setter to update name
    print("Test 3: Updating customer name using property")
    try:
        customer1.name = "Bishesh Kumar Singh"
        print(f"Updated Name: {customer1.name}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 4: Apply discount
    print("Test 4: Applying discount")
    try:
        base_cost = 2500
        discount = customer1.apply_discount(base_cost, 10)
        print(f"Original Cost: ${base_cost:.2f}")
        print(f"With 10% discount: ${discount:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 5: Invalid name (too short)
    print("Test 5: Invalid name - too short")
    try:
        bad_customer = Customer("C003", "Bo", 30, "test@email.com")
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 6: Invalid email
    print("Test 6: Invalid email")
    try:
        bad_customer = Customer("C004", "Jane Smith", 25, "notanemail")
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 7: Invalid age
    print("Test 7: Invalid age")
    try:
        bad_customer = Customer("C005", "Mark Taylor", 15, "mark@email.com")
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 8: Get customer info
    print("Test 8: Customer info")
    info = customer2.get_details()
    print(f"Customer Info: {info}")
    print()

    # Test 9: Child class overriding method
    print("Test 9: Premium customer (method override)")
    try:
        premium_customer = PremiumCustomer("C006", "Rita Rai", 35, "rita@email.com", 850)
        print(f"Success: {premium_customer}")
        print(f"Overridden Details: {premium_customer.get_details()}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    print("="*70)
    print("All tests completed")
    print("="*70)


if __name__ == "__main__":
    run_customer_tests()



"""
Class for managing insurance agents
"""


class Agent:
    """Class for managing insurance agents"""
    
    def __init__(self, agent_id, name, email, commission_rate):
        """Initialize an agent with basic information"""
        self._agent_id = agent_id
        self._name = None
        self._email = None
        self._commission_rate = None
        self._policies_count = 0
        self._total_premium = 0
        
        # Set values using setters for validation
        self.name = name
        self.email = email
        self.commission_rate = commission_rate
    
    # Getter and Setter for name
    @property
    def name(self):
        """Get agent name"""
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Set agent name with validation
        - Must be string
        - Length between 3 and 50 characters
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        
        if len(value) < 3 or len(value) > 50:
            raise ValueError("Name length must be between 3 and 50 characters")
        
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("Name can only contain letters and spaces")
        
        self._name = value
    
    # Getter and Setter for email
    @property
    def email(self):
        """Get agent email"""
        return self._email
    
    @email.setter
    def email(self, value):
        """
        Set agent email with validation
        - Must be string
        - Must have @ and domain
        """
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        
        if '@' not in value or '.' not in value:
            raise ValueError("Email must contain @ and domain extension")
        
        parts = value.split('@')
        if len(parts) != 2:
            raise ValueError("Email format is invalid")
        
        self._email = value
    
    # Getter and Setter for commission_rate
    @property
    def commission_rate(self):
        """Get commission rate"""
        return self._commission_rate
    
    @commission_rate.setter
    def commission_rate(self, rate):
        """
        Set commission rate with validation
        - Must be number between 0 and 100
        """
        if not isinstance(rate, (int, float)):
            raise TypeError("Commission rate must be a number")
        
        if rate < 0 or rate > 100:
            raise ValueError("Commission rate must be between 0 and 100")
        
        self._commission_rate = float(rate)
    
    @property
    def agent_id(self):
        """Get agent ID"""
        return self._agent_id
    
    # Calculation and processing functions
    def calculate_commission(self, premium_amount):
        """Calculate commission on premium amount"""
        if not isinstance(premium_amount, (int, float)):
            raise TypeError("Premium amount must be a number")
        
        commission = premium_amount * (self._commission_rate / 100)
        return round(commission, 2)
    
    def add_policy(self, premium_amount):
        """Add a policy to agent's portfolio"""
        if premium_amount <= 0:
            raise ValueError("Premium amount must be positive")
        
        self._policies_count += 1
        self._total_premium += premium_amount
        return f"Policy added. Total policies: {self._policies_count}"
    
    def calculate_average_premium(self):
        """Calculate average premium per policy"""
        if self._policies_count == 0:
            return 0
        
        average = self._total_premium / self._policies_count
        return round(average, 2)
    
    # Method to be overridden in child class
    def get_agent_performance(self):
        """Get agent performance details"""
        avg_premium = self.calculate_average_premium()
        total_commission = self.calculate_commission(self._total_premium)
        
        performance = {
            "agent_id": self._agent_id,
            "name": self._name,
            "email": self._email,
            "policies_count": self._policies_count,
            "total_premium": self._total_premium,
            "average_premium": avg_premium,
            "commission_rate": self._commission_rate,
            "total_commission": total_commission
        }
        return performance
    
    # String representation
    def __str__(self):
        """Return string representation of agent"""
        return f"Agent: {self._name} ({self._agent_id}), Commission: {self._commission_rate}%"


def run_agent_tests():
    """Run Agent class test cases"""
    print("="*70)
    print("Agent Class Testing")
    print("="*70)
    print()

    # Test 1: Create valid agent
    print("Test 1: Creating valid agent")
    try:
        agent1 = Agent("A001", "Bishesh Kumar", "bishesh.agent@email.com", 5)
        print(f"Success: {agent1}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 2: Create another agent
    print("Test 2: Creating another agent")
    try:
        agent2 = Agent("A002", "Priya Sharma", "priya.agent@email.com", 7.5)
        print(f"Success: {agent2}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 3: Calculate commission
    print("Test 3: Calculating commission")
    try:
        commission = agent1.calculate_commission(10000)
        print(f"Commission on $10,000 at {agent1.commission_rate}%: ${commission:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 4: Add policies to agent
    print("Test 4: Adding policies to agent")
    try:
        agent1.add_policy(1500)
        agent1.add_policy(2000)
        agent1.add_policy(1800)
        print(f"Total Policies: {agent1._policies_count}")
        print(f"Total Premium: ${agent1._total_premium:.2f}")
        print(f"Average Premium: ${agent1.calculate_average_premium():.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 5: Update commission rate
    print("Test 5: Updating commission rate")
    try:
        old_rate = agent1.commission_rate
        agent1.commission_rate = 6
        print(f"Old Rate: {old_rate}%")
        print(f"New Rate: {agent1.commission_rate}%")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 6: Invalid name
    print("Test 6: Invalid name - too short")
    try:
        bad_agent = Agent("A003", "Jo", "jo@email.com", 5)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 7: Invalid commission rate
    print("Test 7: Invalid commission rate - over 100")
    try:
        bad_agent = Agent("A004", "John Smith", "john@email.com", 150)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 8: Invalid email
    print("Test 8: Invalid email format")
    try:
        bad_agent = Agent("A005", "Jane Doe", "notanemail", 5)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 9: Get agent performance
    print("Test 9: Get agent performance details")
    try:
        performance = agent1.get_agent_performance()
        print(f"Performance: {performance}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    print("="*70)
    print("All agent tests completed")
    print("="*70)


if __name__ == "__main__":
    run_agent_tests()



"""
Child class for managing insurance policies
"""


class Policy:
    """Class for managing insurance policies"""
    
    def __init__(self, policy_id, premium, coverage):
        """Initialize a policy with basic information"""
        self._policy_id = policy_id
        self._premium = None
        self._coverage = None
        self._status = "Active"
        
        # Set values using setters for validation
        self.premium = premium
        self.coverage = coverage
    
    # Getter and Setter for premium
    @property
    def premium(self):
        """Get policy premium"""
        return self._premium
    
    @premium.setter
    def premium(self, value):
        """
        Set policy premium with validation
        - Must be positive number
        - Greater than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Premium must be a number")
        
        if value <= 0:
            raise ValueError("Premium must be positive")
        
        self._premium = float(value)
    
    # Getter and Setter for coverage
    @property
    def coverage(self):
        """Get policy coverage amount"""
        return self._coverage
    
    @coverage.setter
    def coverage(self, amount):
        """
        Set policy coverage with validation
        - Must be positive number
        - Greater than 0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Coverage must be a number")
        
        if amount <= 0:
            raise ValueError("Coverage must be positive")
        
        self._coverage = float(amount)
    
    @property
    def policy_id(self):
        """Get policy ID"""
        return self._policy_id
    
    @property
    def status(self):
        """Get policy status"""
        return self._status
    
    # Calculation and processing functions
    def calculate_monthly_premium(self):
        """Calculate monthly premium from annual premium"""
        monthly = self._premium / 12
        return round(monthly, 2)
    
    def calculate_coverage_ratio(self):
        """Calculate ratio of coverage to premium"""
        if self._premium == 0:
            return 0
        ratio = self._coverage / self._premium
        return round(ratio, 2)
    
    # Method to be overridden in child class
    def cancel_policy(self):
        """Cancel the policy"""
        self._status = "Cancelled"
        return f"Policy {self._policy_id} has been cancelled"
    
    # String representation
    def __str__(self):
        """Return string representation of policy"""
        return f"Policy: {self._policy_id}, Premium: ${self._premium:.2f}, Status: {self._status}"


def run_policy_tests():
    """Run Policy class test cases"""
    print("="*70)
    print("Policy Class Testing")
    print("="*70)
    print()

    # Test 1: Create valid policy
    print("Test 1: Creating valid policy")
    try:
        policy1 = Policy("P001", 1500, 500000)
        print(f"Success: {policy1}")
        print(f"Monthly Premium: ${policy1.calculate_monthly_premium():.2f}")
        print(f"Coverage Ratio: {policy1.calculate_coverage_ratio()}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 2: Create another policy
    print("Test 2: Creating another policy")
    try:
        policy2 = Policy("P002", 2000, 750000)
        print(f"Success: {policy2}")
        print(f"Status: {policy2.status}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 3: Update policy premium using property
    print("Test 3: Updating policy premium")
    try:
        old_premium = policy1.premium
        policy1.premium = 2000
        print(f"Old Premium: ${old_premium:.2f}")
        print(f"New Premium: ${policy1.premium:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 4: Cancel policy
    print("Test 4: Cancelling policy")
    try:
        result = policy2.cancel_policy()
        print(f"{result}")
        print(f"New Status: {policy2.status}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 5: Invalid premium (negative)
    print("Test 5: Invalid premium - negative value")
    try:
        bad_policy = Policy("P003", -500, 300000)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 6: Invalid coverage
    print("Test 6: Invalid coverage - zero value")
    try:
        bad_policy = Policy("P004", 1000, 0)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    print("="*70)
    print("All policy tests completed")
    print("="*70)


if __name__ == "__main__":
    run_policy_tests()

"""
Class for managing insurance claims
"""


class Claim:
    """Class for managing insurance claims"""
    
    def __init__(self, claim_id, policy_id, claim_amount):
        """Initialize a claim with basic information"""
        self._claim_id = claim_id
        self._policy_id = policy_id
        self._claim_amount = None
        self._status = "Pending"
        self._approved_amount = 0
        
        # Set values using setters for validation
        self.claim_amount = claim_amount
    
    # Getter and Setter for claim_amount
    @property
    def claim_amount(self):
        """Get claim amount"""
        return self._claim_amount
    
    @claim_amount.setter
    def claim_amount(self, value):
        """
        Set claim amount with validation
        - Must be positive number
        - Greater than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Claim amount must be a number")
        
        if value <= 0:
            raise ValueError("Claim amount must be positive")
        
        self._claim_amount = float(value)
    
    @property
    def claim_id(self):
        """Get claim ID"""
        return self._claim_id
    
    @property
    def status(self):
        """Get claim status"""
        return self._status
    
    @property
    def approved_amount(self):
        """Get approved claim amount"""
        return self._approved_amount
    
    # Calculation and processing functions
    def process_claim(self, approval_percent):
        """Process claim with approval percentage"""
        if approval_percent < 0 or approval_percent > 100:
            raise ValueError("Approval percentage must be between 0 and 100")
        
        self._approved_amount = self._claim_amount * (approval_percent / 100)
        
        if approval_percent == 100:
            self._status = "Approved"
        elif approval_percent == 0:
            self._status = "Rejected"
        else:
            self._status = "Partially Approved"
        
        return round(self._approved_amount, 2)
    
    def calculate_claim_fee(self, fee_percent=5):
        """Calculate processing fee for the claim"""
        fee = self._claim_amount * (fee_percent / 100)
        return round(fee, 2)
    
    # Method to be overridden in child class
    def get_claim_status(self):
        """Get detailed claim status"""
        status_info = {
            "claim_id": self._claim_id,
            "policy_id": self._policy_id,
            "claimed_amount": self._claim_amount,
            "approved_amount": self._approved_amount,
            "status": self._status
        }
        return status_info
    
    # String representation
    def __str__(self):
        """Return string representation of claim"""
        return f"Claim: {self._claim_id}, Amount: ${self._claim_amount:.2f}, Status: {self._status}"


def run_claim_tests():
    """Run Claim class test cases"""
    print("="*70)
    print("Claim Class Testing")
    print("="*70)
    print()

    # Test 1: Create valid claim
    print("Test 1: Creating valid claim")
    try:
        claim1 = Claim("CL001", "P001", 50000)
        print(f"Success: {claim1}")
        print(f"Processing Fee: ${claim1.calculate_claim_fee():.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 2: Create another claim
    print("Test 2: Creating another claim")
    try:
        claim2 = Claim("CL002", "P002", 75000)
        print(f"Success: {claim2}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 3: Process claim with full approval
    print("Test 3: Processing claim - full approval")
    try:
        approved = claim1.process_claim(100)
        print(f"Claimed Amount: ${claim1.claim_amount:.2f}")
        print(f"Approved Amount: ${approved:.2f}")
        print(f"Status: {claim1.status}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 4: Process claim with partial approval
    print("Test 4: Processing claim - partial approval")
    try:
        approved = claim2.process_claim(75)
        print(f"Claimed Amount: ${claim2.claim_amount:.2f}")
        print(f"Approved Amount: ${approved:.2f}")
        print(f"Status: {claim2.status}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 5: Update claim amount using property
    print("Test 5: Updating claim amount")
    try:
        old_amount = claim1.claim_amount
        claim1.claim_amount = 55000
        print(f"Old Amount: ${old_amount:.2f}")
        print(f"New Amount: ${claim1.claim_amount:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 6: Invalid claim amount
    print("Test 6: Invalid claim amount - negative")
    try:
        bad_claim = Claim("CL003", "P003", -25000)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 7: Get claim status
    print("Test 7: Get claim status details")
    try:
        status = claim1.get_claim_status()
        print(f"Claim Status: {status}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    print("="*70)
    print("All claim tests completed")
    print("="*70)


if __name__ == "__main__":
    run_claim_tests()


"""
Class for managing insurance payments
"""


class Payment:
    """Class for managing insurance payments"""
    
    def __init__(self, payment_id, policy_id, amount):
        """Initialize a payment with basic information"""
        self._payment_id = payment_id
        self._policy_id = policy_id
        self._amount = None
        self._payment_method = "Not Specified"
        self._status = "Pending"
        
        # Set values using setters for validation
        self.amount = amount
    
    # Getter and Setter for amount
    @property
    def amount(self):
        """Get payment amount"""
        return self._amount
    
    @amount.setter
    def amount(self, value):
        """
        Set payment amount with validation
        - Must be positive number
        - Greater than 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Payment amount must be a number")
        
        if value <= 0:
            raise ValueError("Payment amount must be positive")
        
        self._amount = float(value)
    
    # Getter and Setter for payment_method
    @property
    def payment_method(self):
        """Get payment method"""
        return self._payment_method
    
    @payment_method.setter
    def payment_method(self, method):
        """
        Set payment method with validation
        - Must be string
        - One of: Card, Bank Transfer, Check, Cash
        """
        valid_methods = ["Card", "Bank Transfer", "Check", "Cash"]
        
        if not isinstance(method, str):
            raise TypeError("Payment method must be a string")
        
        if method not in valid_methods:
            raise ValueError(f"Payment method must be one of {valid_methods}")
        
        self._payment_method = method
    
    @property
    def payment_id(self):
        """Get payment ID"""
        return self._payment_id
    
    @property
    def status(self):
        """Get payment status"""
        return self._status
    
    # Calculation and processing functions
    def process_payment(self):
        """Process the payment"""
        self._status = "Completed"
        return f"Payment {self._payment_id} of ${self._amount:.2f} processed successfully"
    
    def calculate_late_fee(self, days_late):
        """Calculate late fee if payment is overdue"""
        if days_late < 0:
            return 0
        
        # Late fee is 2% per day for first 10 days, then 3% per day
        if days_late <= 10:
            fee = self._amount * 0.02 * days_late
        else:
            fee = (self._amount * 0.02 * 10) + (self._amount * 0.03 * (days_late - 10))
        
        return round(fee, 2)
    
    # Method to be overridden in child class
    def get_payment_details(self):
        """Get payment details"""
        details = {
            "payment_id": self._payment_id,
            "policy_id": self._policy_id,
            "amount": self._amount,
            "method": self._payment_method,
            "status": self._status
        }
        return details
    
    # String representation
    def __str__(self):
        """Return string representation of payment"""
        return f"Payment: {self._payment_id}, Amount: ${self._amount:.2f}, Status: {self._status}"


def run_payment_tests():
    """Run Payment class test cases"""
    print("="*70)
    print("Payment Class Testing")
    print("="*70)
    print()

    # Test 1: Create valid payment
    print("Test 1: Creating valid payment")
    try:
        payment1 = Payment("PM001", "P001", 1500)
        print(f"Success: {payment1}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 2: Create another payment
    print("Test 2: Creating another payment")
    try:
        payment2 = Payment("PM002", "P002", 2000)
        print(f"Success: {payment2}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 3: Set payment method using property
    print("Test 3: Setting payment method")
    try:
        payment1.payment_method = "Card"
        print(f"Payment Method: {payment1.payment_method}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 4: Process payment
    print("Test 4: Processing payment")
    try:
        result = payment1.process_payment()
        print(f"{result}")
        print(f"Status: {payment1.status}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 5: Calculate late fee
    print("Test 5: Calculating late fee")
    try:
        late_fee = payment2.calculate_late_fee(5)
        print(f"Payment Amount: ${payment2.amount:.2f}")
        print(f"Late Fee (5 days): ${late_fee:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 6: Update payment amount
    print("Test 6: Updating payment amount")
    try:
        old_amount = payment2.amount
        payment2.amount = 2500
        print(f"Old Amount: ${old_amount:.2f}")
        print(f"New Amount: ${payment2.amount:.2f}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    # Test 7: Invalid payment method
    print("Test 7: Invalid payment method")
    try:
        payment3 = Payment("PM003", "P003", 1000)
        payment3.payment_method = "Bitcoin"
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 8: Invalid payment amount
    print("Test 8: Invalid payment amount")
    try:
        bad_payment = Payment("PM004", "P004", -500)
    except ValueError as e:
        print(f"Caught validation error: {e}")
        print()

    # Test 9: Get payment details
    print("Test 9: Get payment details")
    try:
        details = payment1.get_payment_details()
        print(f"Payment Details: {details}")
        print()
    except Exception as e:
        print(f"Error: {e}")
        print()

    print("="*70)
    print("All payment tests completed")
    print("="*70)


if __name__ == "__main__":
    run_payment_tests()



"""
Property Insurance Management System - Customer Class
"""




print("="*70)
print("PROPERTY INSURANCE MANAGEMENT SYSTEM - MAIN PROGRAM")
print("="*70)
print()

# Create customers
print("1. Creating Customers")
print("-"*70)
customer1 = Customer("C001", "Alice Brown", 32, "alice@email.com")
customer2 = PremiumCustomer("C002", "Bob Smith", 41, "bob@email.com", 1200)
print(f"✓ {customer1}")
print(f"✓ {customer2}")
print()

# Create policies
print("2. Creating Policies")
print("-"*70)
policy1 = Policy("P001", 1500, 500000)
policy2 = Policy("P002", 2000, 750000)
print(f"✓ {policy1}")
print(f"✓ {policy2}")
print()

# Create agents
print("3. Creating Agents")
print("-"*70)
agent1 = Agent("A001", "Bishesh Kumar", "bishesh.agent@email.com", 5)
agent2 = Agent("A002", "Priya Sharma", "priya.agent@email.com", 7.5)
print(f"✓ {agent1}")
print(f"✓ {agent2}")
print()

# Agents add policies
print("4. Agents Adding Policies")
print("-"*70)
agent1.add_policy(1500)
agent1.add_policy(2000)
agent2.add_policy(1800)
print(f"Agent1 Total Policies: {agent1._policies_count}, Total Premium: ${agent1._total_premium:.2f}")
print(f"Agent2 Total Policies: {agent2._policies_count}, Total Premium: ${agent2._total_premium:.2f}")
print()

# Calculate commissions
print("5. Agent Commissions")
print("-"*70)
comm1 = agent1.calculate_commission(agent1._total_premium)
comm2 = agent2.calculate_commission(agent2._total_premium)
print(f"Agent1 Commission (5%): ${comm1:.2f}")
print(f"Agent2 Commission (7.5%): ${comm2:.2f}")
print()

# Create payments
print("6. Creating Payments")
print("-"*70)
payment1 = Payment("PM001", "P001", 1500)
payment2 = Payment("PM002", "P002", 2000)
payment1.payment_method = "Card"
payment2.payment_method = "Bank Transfer"
print(f"✓ {payment1}")
print(f"✓ {payment2}")
print()

# Process payments
print("7. Processing Payments")
print("-"*70)
result1 = payment1.process_payment()
result2 = payment2.process_payment()
print(f"✓ {result1}")
print(f"✓ {result2}")
print()

# Create claims
print("8. Creating Claims")
print("-"*70)
claim1 = Claim("CL001", "P001", 50000)
claim2 = Claim("CL002", "P002", 75000)
print(f"✓ {claim1}")
print(f"✓ {claim2}")
print()

# Process claims
print("9. Processing Claims")
print("-"*70)
claim1.process_claim(100)
claim2.process_claim(75)
print(f"Claim1 - Claimed: ${claim1.claim_amount:.2f}, Approved: ${claim1.approved_amount:.2f}, Status: {claim1.status}")
print(f"Claim2 - Claimed: ${claim2.claim_amount:.2f}, Approved: ${claim2.approved_amount:.2f}, Status: {claim2.status}")
print()

# Display detailed information
print("10. Detailed Information Summary")
print("-"*70)
print("Customer 1 Details:")
print(f"  {customer1.get_details()}")
print()
print("Customer 2 Details (Overridden):")
print(f"  {customer2.get_details()}")
print()
print("Policy 1 Details:")
print(f"  ID: {policy1.policy_id}, Premium: ${policy1.premium:.2f}, Coverage: ${policy1.coverage:.2f}")
print(f"  Monthly Premium: ${policy1.calculate_monthly_premium():.2f}")
print()
print("Agent 1 Performance:")
agent_perf = agent1.get_agent_performance()
for key, value in agent_perf.items():
    print(f"  {key}: {value}")
print()

# Calculate late fees
print("11. Late Fee Calculation")
print("-"*70)
late_fee = payment1.calculate_late_fee(5)
print(f"Payment1 Late Fee (5 days): ${late_fee:.2f}")
print()

# Insurance cost calculation
print("12. Customer Insurance Cost Calculation")
print("-"*70)
cost1 = customer1.calculate_insurance_cost(500000)
discounted_cost = customer1.apply_discount(cost1, 10)
print(f"Cost for $500,000 property: ${cost1:.2f}")
print(f"After 10% discount: ${discounted_cost:.2f}")
print()

print("="*70)
print("SYSTEM DEMONSTRATION COMPLETED")
print("="*70)
