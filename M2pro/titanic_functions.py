import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    """
    Loads the Titanic.xlsx file into a pandas DataFrame.

    Returns:
        DataFrame if file is found, otherwise None.
    """
    try:
        df = pd.read_excel("Titanic.xlsx")
        return df
    except FileNotFoundError:
        print("ERROR: Titanic.xlsx not found.")
        return None


def display_menu():
    """
    Displays the program menu options to the user.
    """
    print("\nMENU")
    print("1. Display dataset")
    print("2. Get Number of passengers")
    print("3. Get Survived vs Dead")
    print("4. Get Females and/or Males")
    print("5. Get passengers per class")
    print("6. Get Traveled Alone numbers")
    print("7. Get Survived vs Didn't Survive by age group")
    print("8. Exit")


def display_dataset(df):
    """
    Displays the first 15 rows of the DataFrame and plots a heatmap
    of missing values across those rows.
    """
    print(df.head(15))
    plot_dataset(df)


def plot_dataset(df):
    """
    Plots a heatmap showing missing values in the first 15 rows of the dataset.
    """
    fig, ax = plt.subplots(figsize=(12, 5))

    subset = df.head(15).isnull()
    sns.heatmap(
        subset,
        cbar=True,
        cmap="YlOrRd",
        yticklabels=range(1, 16),
        ax=ax
    )

    ax.set_title("Missing Values in First 15 Rows of Titanic Dataset", fontsize=14)
    ax.set_xlabel("Columns", fontsize=11)
    ax.set_ylabel("Row Number", fontsize=11)
    plt.tight_layout()
    plt.legend(
        handles=[
            plt.Rectangle((0, 0), 1, 1, color="#d73027", label="Missing"),
            plt.Rectangle((0, 0), 1, 1, color="#ffffbf", label="Present"),
        ],
        loc="upper right",
        bbox_to_anchor=(1.15, 1),
        title="Value Status"
    )
    plt.savefig("dataset_preview.png", bbox_inches="tight")
    print("Plot saved as dataset_preview.png")
    plt.show()


def count_records(df):
    """
    Prints the total number of passengers in the dataset and plots a bar
    summarizing total count.
    """
    print("Total passengers:", len(df))
    plot_count_records(df)


def plot_count_records(df):
    """
    Plots a bar chart showing the total number of passengers in the dataset.
    """
    fig, ax = plt.subplots(figsize=(5, 5))

    data = pd.DataFrame({"Category": ["Total Passengers"], "Count": [len(df)]})
    sns.barplot(data=data, x="Category", y="Count", hue="Category",
                palette=["steelblue"], ax=ax, legend=False)

    ax.set_title("Total Number of Passengers", fontsize=14)
    ax.set_xlabel("Category", fontsize=11)
    ax.set_ylabel("Count", fontsize=11)
    ax.bar_label(ax.containers[0], fontsize=12)
    ax.legend(
        handles=[plt.Rectangle((0, 0), 1, 1, color="steelblue", label="Passengers")],
        loc="upper right",
        title="Legend"
    )
    plt.tight_layout()
    plt.savefig("passenger_count.png", bbox_inches="tight")
    print("Plot saved as passenger_count.png")
    plt.show()


def survived_vs_dead(df):
    """
    Displays the number of passengers who survived vs did not survive.
    """
    counts = df["survived"].value_counts()
    print("Survived:", counts.get(1, 0))
    print("Did not survive:", counts.get(0, 0))
    plot_survived_vs_dead(df)


def plot_survived_vs_dead(df):
    """
    Plots a count bar chart of survivors vs non-survivors.
    """
    plot_df = df.copy()
    plot_df["Survival Status"] = plot_df["survived"].map({1: "Survived", 0: "Did Not Survive"})

    fig, ax = plt.subplots(figsize=(7, 5))
    palette = {"Survived": "#2ecc71", "Did Not Survive": "#e74c3c"}

    sns.countplot(data=plot_df, x="Survival Status", hue="Survival Status",
                  palette=palette, ax=ax, legend=True)

    ax.set_title("Survived vs Did Not Survive", fontsize=14)
    ax.set_xlabel("Survival Status", fontsize=11)
    ax.set_ylabel("Number of Passengers", fontsize=11)
    ax.bar_label(ax.containers[0], fontsize=11)
    ax.legend(title="Survival Status", loc="upper right")
    plt.tight_layout()
    plt.savefig("survived_vs_dead.png", bbox_inches="tight")
    print("Plot saved as survived_vs_dead.png")
    plt.show()


def gender_stats(df):
    """
    Displays survival statistics for females, males, or both.
    """
    choice = ""
    while choice not in ["female", "male", "both"]:
        choice = input("Enter female, male, or both: ").strip().lower()
        if choice not in ["female", "male", "both"]:
            print("Invalid option. Try again.")

    if choice == "female":
        data = df[df["gender"] == "female"]["survived"].value_counts()
        print("Females Survived:", data.get(1, 0))
        print("Females Died:", data.get(0, 0))

    elif choice == "male":
        data = df[df["gender"] == "male"]["survived"].value_counts()
        print("Males Survived:", data.get(1, 0))
        print("Males Died:", data.get(0, 0))

    else:
        for g in ["female", "male"]:
            data = df[df["gender"] == g]["survived"].value_counts()
            print(f"\n{g.title()} Survived:", data.get(1, 0))
            print(f"{g.title()} Died:", data.get(0, 0))

    plot_gender_stats(df, choice)


def plot_gender_stats(df, choice):
    """
    Plots a grouped bar chart of survival by gender based on the user's choice.
    """
    plot_df = df.copy()
    plot_df["Survival Status"] = plot_df["survived"].map({1: "Survived", 0: "Did Not Survive"})

    if choice == "both":
        filtered = plot_df
        title = "Survival by Gender (Female & Male)"
        filename = "gender_stats_both.png"
    else:
        filtered = plot_df[plot_df["gender"] == choice]
        title = f"Survival Stats – {choice.title()}"
        filename = f"gender_stats_{choice}.png"

    fig, ax = plt.subplots(figsize=(8, 5))
    palette = {"Survived": "#2ecc71", "Did Not Survive": "#e74c3c"}

    sns.countplot(
        data=filtered,
        x="gender",
        hue="Survival Status",
        palette=palette,
        ax=ax
    )

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Gender", fontsize=11)
    ax.set_ylabel("Number of Passengers", fontsize=11)
    for container in ax.containers:
        ax.bar_label(container, fontsize=10)
    ax.legend(title="Survival Status", loc="upper right")
    plt.tight_layout()
    plt.savefig(filename, bbox_inches="tight")
    print(f"Plot saved as {filename}")
    plt.show()


def class_stats(df):
    """
    Displays statistics for each passenger class.
    """
    print("\nClass | Total | Survived | Died")
    print("---------------------------------")

    for cls in sorted(df["pclass"].unique()):
        total = len(df[df["pclass"] == cls])
        survived = len(df[(df["pclass"] == cls) & (df["survived"] == 1)])
        died = len(df[(df["pclass"] == cls) & (df["survived"] == 0)])
        print(f"{cls:^5} | {total:^5} | {survived:^8} | {died:^4}")

    plot_class_stats(df)


def plot_class_stats(df):
    """
    Plots a grouped bar chart of survival counts per passenger class.
    """
    plot_df = df.copy()
    plot_df["Survival Status"] = plot_df["survived"].map({1: "Survived", 0: "Did Not Survive"})
    plot_df["pclass"] = plot_df["pclass"].map({1: "1st Class", 2: "2nd Class", 3: "3rd Class"})

    fig, ax = plt.subplots(figsize=(9, 5))
    palette = {"Survived": "#2ecc71", "Did Not Survive": "#e74c3c"}

    sns.countplot(
        data=plot_df,
        x="pclass",
        hue="Survival Status",
        palette=palette,
        ax=ax
    )

    ax.set_title("Survival by Passenger Class", fontsize=14)
    ax.set_xlabel("Passenger Class", fontsize=11)
    ax.set_ylabel("Number of Passengers", fontsize=11)
    for container in ax.containers:
        ax.bar_label(container, fontsize=10)
    ax.legend(title="Survival Status", loc="upper right")
    plt.tight_layout()
    plt.savefig("class_stats.png", bbox_inches="tight")
    print("Plot saved as class_stats.png")
    plt.show()


def traveling_alone_stats(df):
    """
    Displays survival statistics for passengers who traveled alone
    versus those who did not travel alone.
    """
    print("\nTraveling Alone Stats")

    for val in [0, 1]:
        group = df[df["Traveling Alone"] == val]
        survived = len(group[group["survived"] == 1])
        died = len(group[group["survived"] == 0])
        total = len(group)

        percent = (survived / total) * 100 if total > 0 else 0
        label = "Not Alone" if val == 0 else "Alone"

        print(f"\n{label}:")
        print("Survived:", survived)
        print("Died:", died)
        print("Survival %:", round(percent, 2))

    plot_traveling_alone_stats(df)


def plot_traveling_alone_stats(df):
    """
    Plots a grouped bar chart comparing survival for passengers
    traveling alone vs. not alone.
    """
    plot_df = df.copy()
    plot_df["Survival Status"] = plot_df["survived"].map({1: "Survived", 0: "Did Not Survive"})
    plot_df["Travel Group"] = plot_df["Traveling Alone"].map({1: "Alone", 0: "Not Alone"})

    fig, ax = plt.subplots(figsize=(8, 5))
    palette = {"Survived": "#2ecc71", "Did Not Survive": "#e74c3c"}

    sns.countplot(
        data=plot_df,
        x="Travel Group",
        hue="Survival Status",
        palette=palette,
        ax=ax
    )

    ax.set_title("Survival by Travel Group (Alone vs Not Alone)", fontsize=14)
    ax.set_xlabel("Travel Group", fontsize=11)
    ax.set_ylabel("Number of Passengers", fontsize=11)
    for container in ax.containers:
        ax.bar_label(container, fontsize=10)
    ax.legend(title="Survival Status", loc="upper right")
    plt.tight_layout()
    plt.savefig("travel_alone.png", bbox_inches="tight")
    print("Plot saved as travel_alone.png")
    plt.show()


def age_group_stats(df):
    """
    Displays survival statistics for a selected age group.
    """
    age_groups = df["Age Group"].dropna().unique()

    print("Available age groups:")
    for ag in age_groups:
        print("-", ag)

    lower_groups = [ag.lower() for ag in age_groups]

    choice = ""
    while choice not in lower_groups:
        choice = input("Enter age group: ").strip().lower()
        if choice not in lower_groups:
            print("Invalid age group. Try again.")

    real_value = age_groups[lower_groups.index(choice)]

    group = df[df["Age Group"] == real_value]
    survived = len(group[group["survived"] == 1])
    died = len(group[group["survived"] == 0])
    total = len(group)

    percent = (survived / total) * 100 if total > 0 else 0

    print("\nSurvived:", survived)
    print("Did not survive:", died)
    print("Survival %:", round(percent, 2))

    plot_age_group_stats(df, real_value)


def plot_age_group_stats(df, selected_group):
    """
    Plots a grouped bar chart showing survival for all age groups,
    highlighting the selected group.
    """
    plot_df = df.copy()
    plot_df["Survival Status"] = plot_df["survived"].map({1: "Survived", 0: "Did Not Survive"})

    fig, ax = plt.subplots(figsize=(11, 5))
    palette = {"Survived": "#2ecc71", "Did Not Survive": "#e74c3c"}

    order = sorted(plot_df["Age Group"].dropna().unique())

    sns.countplot(
        data=plot_df,
        x="Age Group",
        hue="Survival Status",
        palette=palette,
        order=order,
        ax=ax
    )

    ax.set_title(f"Survival by Age Group  (Selected: {selected_group})", fontsize=14)
    ax.set_xlabel("Age Group", fontsize=11)
    ax.set_ylabel("Number of Passengers", fontsize=11)
    plt.xticks(rotation=20, ha="right")
    for container in ax.containers:
        ax.bar_label(container, fontsize=9)
    ax.legend(title="Survival Status", loc="upper right")
    plt.tight_layout()

    safe_name = selected_group.replace(" ", "_").replace("/", "-").lower()
    filename = f"age_group_{safe_name}.png"
    plt.savefig(filename, bbox_inches="tight")
    print(f"Plot saved as {filename}")
    plt.show()
