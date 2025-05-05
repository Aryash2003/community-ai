import json
import random
import time

class VoiceCommandSimulator:
    """
    Simulates voice commands by generating appropriately formatted
    text that mimics what would come from a speech-to-text system.
    """
    
    def __init__(self, language="en-US", confidence_range=(0.85, 0.98), supported_languages=None):
        self.language = language
        self.confidence_range = confidence_range
        self.supported_languages = supported_languages or ["en-US", "hi-IN", "ta-IN"]
        
        # Common words that might be misheard
        self.sound_alikes = {
            "balance": ["balance", "ballance", "valance"],
            "account": ["account", "a count", "a mount"],
            "transfer": ["transfer", "transfers", "transferred"],
            "fifty": ["fifty", "15", "15 t", "fifth"],
            "dollars": ["dollars", "dollar", "dollers"],
            "recent": ["recent", "resent", "reason"],
            "transactions": ["transactions", "transaction", "trans actions"]
        }
    
    def generate_voice_result(self, command_text):
        """
        Generate a simulated voice recognition result from a command text
        Returns a dict similar to what a speech-to-text API would return
        """
        # Add some randomness to simulate actual speech recognition
        words = command_text.split()
        processed_words = []
        
        for word in words:
            # Check if this word has common sound-alikes
            if word.lower() in self.sound_alikes:
                # 20% chance to use a sound-alike instead
                if random.random() < 0.2:
                    processed_words.append(random.choice(self.sound_alikes[word.lower()]))
                else:
                    processed_words.append(word)
            else:
                processed_words.append(word)
        
        # Join words back into a string
        recognized_text = " ".join(processed_words)
        
        # Generate a confidence score within the specified range
        confidence = random.uniform(self.confidence_range[0], self.confidence_range[1])
        
        # Create a result object similar to what speech-to-text APIs return
        result = {
            "results": [
                {
                    "alternatives": [
                        {
                            "transcript": recognized_text,
                            "confidence": confidence
                        }
                    ],
                    "is_final": True
                }
            ],
            "language": self.language,
            "processing_time_ms": random.randint(100, 500)
        }
        
        return result
    
    def simulate_intent_recognition(self, command_text):
        """
        Simulate NLP intent recognition by returning an intent label
        based on keywords in the command text.
        """
        command_text_lower = command_text.lower()
        if "balance" in command_text_lower:
            return "balance_inquiry"
        elif "transfer" in command_text_lower or "pay" in command_text_lower:
            return "fund_transfer"
        elif "transaction" in command_text_lower or "history" in command_text_lower:
            return "transaction_history"
        else:
            return "unknown_intent"
    
    def simulate_voice_biometrics(self, command_text):
        """
        Simulate voice biometric authentication.
        For now, randomly succeed or fail with high probability of success.
        """
        # 90% chance of successful biometric authentication
        success = random.random() < 0.9
        return success
    
    def simulate_command(self, command_text):
        """
        Simulate the process of speaking a command, with realistic timing
        Returns the simulated recognition result including intent and biometric info
        """
        # Simulate the time it takes to speak the command
        speaking_time = 0.1 * len(command_text.split())  # ~100ms per word
        time.sleep(speaking_time)
        
        # Simulate processing delay
        processing_delay = random.uniform(0.2, 0.8)  # 200-800ms
        time.sleep(processing_delay)
        
        # Generate voice recognition result
        voice_result = self.generate_voice_result(command_text)
        
        # Simulate intent recognition
        intent = self.simulate_intent_recognition(command_text)
        
        # Simulate voice biometric authentication
        biometric_success = self.simulate_voice_biometrics(command_text)
        
        # Add intent and biometric info to the result
        voice_result["intent"] = intent
        voice_result["biometric_success"] = biometric_success
        
        return voice_result

def test_simulator():
    """Test the voice command simulator with sample commands"""
    simulator = VoiceCommandSimulator()
    
    # Sample commands
    commands = [
        "What is my account balance",
        "Transfer 50 dollars to John Doe",
        "Show my recent transactions"
    ]
    
    # Simulate each command and print the result
    for command in commands:
        print(f"Original command: '{command}'")
        result = simulator.simulate_command(command)
        print(f"Simulated result: '{result['results'][0]['alternatives'][0]['transcript']}'")
        print(f"Confidence: {result['results'][0]['alternatives'][0]['confidence']:.2f}")
        print(f"Intent: {result['intent']}")
        print(f"Biometric Success: {result['biometric_success']}")
        print(f"Processing time: {result['processing_time_ms']}ms")
        print("-" * 50)

if __name__ == "__main__":
    test_simulator()
