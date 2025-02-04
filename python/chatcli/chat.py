import sys
import os
from typing import List, Optional
from datetime import datetime

class Message:
    def __init__(self, content: str, is_user: bool):
        self.content = content
        self.is_user = is_user
        self.timestamp = datetime.now()

class ChatCallback:
    def process_message(self, message: Message) -> Message:
        """Process a message before it's displayed"""
        return message

class Chat:
    def __init__(self):
        self.callbacks: List[ChatCallback] = []
        self.running = True
        
        # Enable command history if running on Unix-like systems
        if os.name == 'posix':
            import readline
    
    def register_callback(self, callback: ChatCallback) -> None:
        """Register a new callback for message processing"""
        self.callbacks.append(callback)
    
    def process_message(self, message: Message) -> Message:
        """Run message through all registered callbacks"""
        for callback in self.callbacks:
            message = callback.process_message(message)
        return message
    
    def display_message(self, message: Message) -> None:
        """Display a message in the terminal"""
        prefix = ">" if message.is_user else ">>"
        print(f"\n{prefix} {message.content}")
    
    def get_user_input(self) -> Optional[str]:
        """Get input from the user"""
        try:
            return input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            return None
    
    def run(self) -> None:
        """Main chat loop"""
        print("\nWelcome to the Chat CLI! Type 'q' to quit.")
        
        while self.running:
            user_input = self.get_user_input()
            
            if user_input is None or user_input.lower() == 'q':
                self.running = False
                print("\nGoodbye!")
                break
            
            if not user_input:
                continue
            
            # Process and display user message
            user_message = Message(user_input, is_user=True)
            processed_user_message = self.process_message(user_message)
            self.display_message(processed_user_message)

def main():
    # Example usage with a simple callback
    class UppercaseCallback(ChatCallback):
        def process_message(self, message: Message) -> Message:
            message.content = message.content.upper()
            message.is_user=False
            return message
    
    chat = Chat()
    chat.register_callback(UppercaseCallback())
    chat.run()

if __name__ == "__main__":
    main() 