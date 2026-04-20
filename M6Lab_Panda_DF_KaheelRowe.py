# Kaheel Rowe
# This program will display the survivors and non-survivors of the Titanic
# with seaborn visualizations for each menu option.
# CSC221 M6Lab
# 04/19/2026

import titanic_functions as tf


def main():
    df = tf.load_data()
    if df is None:
        return

    choice = ""
    while choice != "8":
        tf.display_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                tf.display_dataset(df)
            elif choice == "2":
                tf.count_records(df)
            elif choice == "3":
                tf.survived_vs_dead(df)
            elif choice == "4":
                tf.gender_stats(df)
            elif choice == "5":
                tf.class_stats(df)
            elif choice == "6":
                tf.traveling_alone_stats(df)
            elif choice == "7":
                tf.age_group_stats(df)
            elif choice == "8":
                print("Thank you for using the program!")
            else:
                print("Invalid menu choice.")
        except Exception as e:
            print("An error occurred:", e)


main()
