import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load data
day_df_data = pd.read_csv('day_df_data.csv')
hour_df_data = pd.read_csv('hour_df_data.csv')
day_df_data['dteday'] = pd.to_datetime(day_df_data['dteday'])

#Page title
st.title('Bike Sharing Analysis Dashboard')

#Sidebar menu
menu = st.sidebar.radio("Menu", ["Overview", "Exploratory Data Analysis"])

if menu == "Overview":
    st.header("Dataset Overview")
    st.write("This dashboard presents insights into the bike sharing dataset.")

    st.subheader("Day Dataset")
    st.write(day_df_data.head())

    st.subheader("Hour Dataset")
    st.write(hour_df_data.head())

    st.write("Dataset Information")
    st.write("Day Dataset:")
    st.write(day_df_data.info())
    st.write("Hour Dataset:")
    st.write(hour_df_data.info())

elif menu == "Exploratory Data Analysis":
    st.header("Exploratory Data Analysis")

    st.subheader("Rental Trends Based on Date Range")
    start_date = st.sidebar.date_input("Start Date", day_df_data['dteday'].min())
    end_date = st.sidebar.date_input("End Date", day_df_data['dteday'].max())

    if start_date > end_date:
        st.error("Start date must be before end date!")
    else:
        filtered_data = day_df_data[(day_df_data['dteday'] >= pd.to_datetime(start_date)) & (day_df_data['dteday'] <= pd.to_datetime(end_date))]
        st.write(f"Data from {start_date} to {end_date}")

        plt.figure(figsize=(10, 6))
        sns.lineplot(x='dteday', y='cnt', data=filtered_data, marker="o")
        plt.title("Bike Rentals Over Selected Date Range")
        plt.xlabel("Date")
        plt.ylabel("Total Rentals")
        plt.xticks(rotation=45)
        st.pyplot(plt)

    st.subheader("Distribution of Bike Rentals (Hourly)")

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hour_df_data, x='hr', y='cnt', marker='o', color='b')
    plt.title('Average Bike Rentals by Hour')
    plt.xlabel('Hour')
    plt.ylabel('Average Rentals')
    plt.xticks(range(0, 24))
    plt.grid(True)
    st.pyplot(plt)

    st.subheader("Factors Influencing Daily Rentals")
    #Impact of Weather on Rentals
    st.subheader("Impact of Weather on Rentals")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=day_df_data, palette="muted")
    plt.title("Impact of Weather on Daily Rentals")
    plt.xlabel("Weather Situation")
    plt.ylabel("Bike Rentals")
    st.pyplot(plt)

    #Impact of Season on Rentals
    st.subheader("Impact of Season on Rentals")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='cnt', data=day_df_data, palette="coolwarm")
    plt.title("Impact of Season on Daily Rentals")
    plt.xlabel("Season")
    plt.ylabel("Bike Rentals")
    st.pyplot(plt)

    #Impact of Temperature on Rentals
    st.subheader("Impact of Temperature on Rentals")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_df_data, hue='season', palette="coolwarm")
    plt.title("Impact of Temperature on Daily Rentals")
    plt.xlabel("Temperature")
    plt.ylabel("Bike Rentals")
    st.pyplot(plt)

    #Rentals on Working Days vs Holidays
    st.subheader("Rentals on Working Days vs Holidays")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='workingday', y='cnt', data=day_df_data, palette="Set2")
    plt.title("Bike Rentals: Working Days vs Holidays")
    plt.xlabel("Working Day (1: Yes, 0: No)")
    plt.ylabel("Bike Rentals")
    st.pyplot(plt)

#Footer
st.sidebar.text("Developed by Komang Agus Wira Adnyana")
