import streamlit as st
from scipy.stats import t, norm, f, chi2

# Streamlit App Title
st.title("Critical Value and P-Value Calculator")

# User selection: Critical Value or P-Value
calc_type = st.radio("What do you want to calculate?", ("Critical Value", "P-Value"))

# Sidebar for selecting distribution and tail type
dist_type = st.sidebar.selectbox(
    "Select Distribution",
    ("t-distribution", "z-distribution", "F-distribution", "Chi-Square distribution")
)

# Tail type is fixed to Right-Tailed for F and Chi-Square
tail_type = "Right-Tailed" if dist_type in ["F-distribution", "Chi-Square distribution"] else st.sidebar.radio("Select Tail Type", ("Right-Tailed", "Left-Tailed", "Two-Tailed"))

# Common input for significance level
alpha = st.number_input("Enter significance level (alpha)", min_value=0.0001, max_value=0.5, step=0.01, value=0.05)
effective_alpha = alpha if tail_type != "Two-Tailed" else alpha / 2

# Display message for F and Chi-Square distributions
if dist_type in ["F-distribution", "Chi-Square distribution"]:
    st.write("**Note:** Only Right-Tailed critical values are shown for this distribution.")

# Logic for Critical Value calculation
if calc_type == "Critical Value":
    if dist_type == "t-distribution":
        st.subheader("t-Distribution Critical Value")
        df = st.number_input("Enter degrees of freedom (df)", min_value=1, step=1, value=10)
        critical_t = t.ppf(1 - effective_alpha, df)
        if tail_type == "Two-Tailed":
            st.write(f"Critical t-value: ±{critical_t:.4f}")
        elif tail_type == "Right-Tailed":
            st.write(f"Critical t-value (Right): {critical_t:.4f}")
        elif tail_type == "Left-Tailed":
            st.write(f"Critical t-value (Left): {-critical_t:.4f}")

    elif dist_type == "z-distribution":
        st.subheader("z-Distribution Critical Value")
        critical_z = norm.ppf(1 - effective_alpha)
        if tail_type == "Two-Tailed":
            st.write(f"Critical z-value: ±{critical_z:.4f}")
        elif tail_type == "Right-Tailed":
            st.write(f"Critical z-value (Right): {critical_z:.4f}")
        elif tail_type == "Left-Tailed":
            st.write(f"Critical z-value (Left): {-critical_z:.4f}")

    elif dist_type == "F-distribution":
        st.subheader("F-Distribution Critical Value")
        dfn = st.number_input("Enter degrees of freedom (numerator, dfn)", min_value=1, step=1, value=1)
        dfd = st.number_input("Enter degrees of freedom (denominator, dfd)", min_value=1, step=1, value=10)
        critical_f = f.ppf(1 - effective_alpha, dfn, dfd)
        st.write(f"Critical F-value: {critical_f:.4f}")

    elif dist_type == "Chi-Square distribution":
        st.subheader("Chi-Square Distribution Critical Value")
        df = st.number_input("Enter degrees of freedom (df)", min_value=1, step=1, value=10)
        critical_chi2 = chi2.ppf(1 - effective_alpha, df)
        st.write(f"Critical Chi-Square value: {critical_chi2:.4f}")

# Logic for P-Value calculation
elif calc_type == "P-Value":
    if dist_type == "t-distribution":
        st.subheader("t-Distribution P-Value")
        df = st.number_input("Enter degrees of freedom (df)", min_value=1, step=1, value=10)
        t_value = st.number_input("Enter test statistic (t-value)", value=0.0)
        if tail_type == "Two-Tailed":
            p_value = 2 * (1 - t.cdf(abs(t_value), df))
        elif tail_type == "Right-Tailed":
            p_value = 1 - t.cdf(t_value, df)
        elif tail_type == "Left-Tailed":
            p_value = t.cdf(t_value, df)
        st.write(f"P-value: {p_value:.4f}")

    elif dist_type == "z-distribution":
        st.subheader("z-Distribution P-Value")
        z_value = st.number_input("Enter test statistic (z-value)", value=0.0)
        if tail_type == "Two-Tailed":
            p_value = 2 * (1 - norm.cdf(abs(z_value)))
        elif tail_type == "Right-Tailed":
            p_value = 1 - norm.cdf(z_value)
        elif tail_type == "Left-Tailed":
            p_value = norm.cdf(z_value)
        st.write(f"P-value: {p_value:.4f}")

    elif dist_type == "F-distribution":
        st.subheader("F-Distribution P-Value")
        dfn = st.number_input("Enter degrees of freedom (numerator, dfn)", min_value=1, step=1, value=1)
        dfd = st.number_input("Enter degrees of freedom (denominator, dfd)", min_value=1, step=1, value=10)
        f_value = st.number_input("Enter test statistic (F-value)", value=0.0)
        p_value = 1 - f.cdf(f_value, dfn, dfd)
        st.write(f"P-value: {p_value:.4f}")

    elif dist_type == "Chi-Square distribution":
        st.subheader("Chi-Square Distribution P-Value")
        df = st.number_input("Enter degrees of freedom (df)", min_value=1, step=1, value=10)
        chi2_value = st.number_input("Enter test statistic (Chi-Square value)", value=0.0)
        p_value = 1 - chi2.cdf(chi2_value, df)
        st.write(f"P-value: {p_value:.4f}")

# AdSense Script
st.markdown(
    """
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2205114276182850"
         crossorigin="anonymous"></script>
    """,
    unsafe_allow_html=True
)

# Footer
st.write("---")
st.write("This calculator uses scipy.stats to compute critical values and p-values.")
