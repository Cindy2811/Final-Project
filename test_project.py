import pytest
import project

def test_calculate_bmi():
    # Test with known values
    bmi = project.calculate_bmi(70, 1.75)
    assert abs(bmi - 22.857142857142858) < 0.0001
    bmi = project.calculate_bmi(50, 1.60)
    assert abs(bmi - 19.53125) < 0.0001

def test_evaluate_bmi():
    # Verify BMI categories based on BMI values
    assert project.evaluate_bmi(17) == "Underweight"
    assert project.evaluate_bmi(22) == "Normal weight"
    assert project.evaluate_bmi(27) == "Overweight"
    assert project.evaluate_bmi(32) == "Obesity"

def test_evaluate_diet():
    # If the goal is gain, it recommends "Caloric Surplus"
    assert project.evaluate_diet(22, "gain", "medium", "none", "no") == "Caloric Surplus"
    # If the goal is lose, it recommends "Caloric Deficit"
    assert project.evaluate_diet(27, "lose", "high", "none", "yes") == "Caloric Deficit"
    # If the goal is maintain, it recommends "Maintenance"
    assert project.evaluate_diet(23, "maintain", "low", "none", "no") == "Maintenance"
    # Unrecognized goal
    assert project.evaluate_diet(23, "other", "low", "none", "no") == "Unrecognized goal"
