from model import train_model

# Train model
model, accuracy = train_model()

print("Model Accuracy:", accuracy)

# Example passenger data
# Format: [Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]
sample = [[3, 0, 22, 1, 0, 7.25, 2]]

# Predict
prediction = model.predict(sample)

if prediction[0] == 1:
    print("Result: Survived")
else:
    print("Result: Not Survived")