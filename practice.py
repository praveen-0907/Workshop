def find_s(training_data, attributes):
    print("Training Dataset:")
    # Header for the dataset
    header = " ".join(attributes) + " enjoySport"
    print(f"      {header}")
    for i, row in enumerate(training_data):
        print(f"{i}  {' '.join(row)}")
    print("-" * 70)
    
    print("\nFIND-S Algorithm Execution:\n")
    
    hypothesis = None
    step = 1

    for example in training_data:
        features = example[:-1]
        target = example[-1]

        if target == "Yes":
            if hypothesis is None:
                # Step 1: Initialize with first positive example
                hypothesis = list(features)
                print(f"Step {step}: Initialize hypothesis with first positive example")
                print(f"Hypothesis: {hypothesis}\n")
            else:
                # Processing subsequent positive examples
                print(f"Step {step}: Processing positive example: {features}")
                for i in range(len(hypothesis)):
                    if hypothesis[i] != features[i]:
                        hypothesis[i] = "?"
                print(f"Updated Hypothesis: {hypothesis}\n")
            step += 1
        else:
            # Step for skipping negative examples
            print(f"Step {step}: Skipping negative example: {features}")
            print("-" * 5) # Visual separator for skipped steps in some formats
            step += 1

    return hypothesis

# Defining the dataset based on your provided list
attributes = ["Sky", "Temp", "Humid", "Wind", "Water", "Forecast"]
training_data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"],
    ["Cloudy", "Mild", "Normal", "Weak", "Warm", "Same", "Yes"],
    ["Cloudy", "Cold", "High", "Strong", "Cool", "Change", "No"],
    ["Sunny", "Mild", "High", "Weak", "Warm", "Same", "Yes"],
    ["Rainy", "Warm", "Normal", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Cold", "Normal", "Weak", "Cool", "Same", "Yes"],
    ["Cloudy", "Warm", "High", "Strong", "Warm", "Same", "Yes"]
]

print("71812401155 - Praveen N")
print("===================================")
final_h = find_s(training_data, attributes)

print("=" * 70)
print("FINAL MOST SPECIFIC HYPOTHESIS:")
print("=" * 70)
for attr, val in zip(attributes, final_h):
    print(f"{attr}: {val}")
print("=" * 70)

print("\nInterpretation:")
print("=" * 70)
print("'?' means the attribute can take any value")
print("Specific value means that attribute must have that exact value")