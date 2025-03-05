# Final-Project
BMI Calculator and Diet Recommendation Project
Video Demo:
Description:
BMI Calculator:
This module prompts the user to enter their gender, age, weight, and height, then calculates the BMI using the formula:

BMI = weight / height²

After calculating the BMI, the result is classified into one of four categories based on global health standards: •⁠ ⁠Underweight •⁠ ⁠Normal weight •⁠ ⁠Overweight •⁠ ⁠Obesity

The module provides immediate feedback, displaying both the numerical BMI value and the corresponding health category, helping users better understand their health status.

Dietary Recommendation:
In this module, users enter additional information about their lifestyle and dietary goals. By answering four questions regarding their main fitness objective (e.g., gaining, losing, or maintaining weight), physical activity level, dietary restrictions, and food preferences, the system provides a personalized meal plan. The recommendations include: •⁠ ⁠Caloric surplus (for those looking to gain weight) •⁠ ⁠Caloric deficit (for those aiming to lose weight) •⁠ ⁠Maintenance (for those who want to keep their current weight)

The application's design is kept simple: through a main menu, the user can choose between the BMI Calculator, Dietary Recommendation, or exit the program.

Project Structure
The repository is organized into the following key files: •⁠ ⁠project.py: Contains all functions for BMI calculation, BMI evaluation, and dietary recommendation logic. It also includes interactive menus for the BMI and Diet modules, along with the main menu that connects everything. •⁠ ⁠test_project.py: Contains tests for the project's critical non-interactive functions (e.g., BMI calculation and evaluation). This code was written using the pytest framework to ensure the core functionalities work correctly. •⁠ ⁠requirements.txt: Lists the project's dependencies.

Detailed Features
BMI Calculator Module
The BMI Calculator module requires the following user inputs: •⁠ ⁠Gender: While it does not currently affect the calculation, it is recorded for future expansions (e.g., gender-specific health recommendations). •⁠ ⁠Age: This significantly impacts calculations and helps personalize recommendations or provide better age-based dietary advice. •⁠ ⁠Weight (kg) and Height (meters): These values are used to compute the BMI.

The calculate_bmi() function computes the BMI, while the evaluate_bmi() function classifies it based on predefined thresholds. After calculation, the system displays both the BMI value and the corresponding category (e.g., "Underweight," "Normal," "Overweight," or "Obesity").

Dietary Recommendation Module
After obtaining the BMI, the Diet module guides the user through four questions to refine the nutritional advice. These questions cover: •⁠ ⁠Main fitness goal: Options include "gain" (to build muscle mass), "lose" (to reduce body fat), or "maintain" (to keep the current weight). •⁠ ⁠Physical activity level: Low, medium, or high levels to determine caloric needs. •⁠ ⁠Dietary restrictions: Information on specific diets (e.g., no restrictions, vegetarian, vegan, or other special diets) to personalize suggestions. •⁠ ⁠Food preferences: If the user prefers eating more at certain times of the day, which can influence meal planning.

Based on these inputs and the calculated BMI, the evaluate_diet() function suggests a dietary approach, recommending a caloric surplus, deficit, or maintenance plan. This personalized approach helps users align their diet with their fitness goals.

Design Decisions
During the design phase, several key decisions were made: •⁠ ⁠Modularity: The code is divided into separate functions for BMI calculation, evaluation, and dietary recommendation. This makes the code easier to maintain and allows for more effective testing. •⁠ ⁠User Interaction: A simple text-based menu system was implemented to guide users through the various modules. This ensures a clear, structured, and detailed experience. •⁠ ⁠Testing: Critical functions are covered by unit tests using the pytest framework, ensuring the accuracy of calculations and classifications. •⁠ ⁠Expandability: Although the current version only handles BMI and basic dietary recommendations, the structure allows for future expansions (e.g., more detailed meal plans, integration with external APIs for health data, or advanced analytics based on user input).
