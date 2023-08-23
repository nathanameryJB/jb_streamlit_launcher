import streamlit as st
import webbrowser


def main():
    # Embed the Google Font link for "Nixie One" and set the title's font.
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@100;400&display=swap');

            /* Applying the font to the entire body */
            body p {
                font-family: 'josefin sans', sans-serif !important;
            }
            
            @import url('https://fonts.googleapis.com/css2?family=Nixie+One&display=swap');
            .nixie-font {
                font-family: 'Nixie One', cursive;
            }
            .title-container {
                display: flex;
                align-items: center;
                margin-bottom:50px
            }
            .title-container img {
                width: 50px;
                margin-right: 30px;

            }
            .title-container h1 {
                color: #fff;
                margin: 0px ;
                padding: 0px;
                vertical-align: middle;
            }
                  
        </style>
        """,
        unsafe_allow_html=True
    )



    # Use the "Nixie One" font for the title along with the icon
    st.markdown(
        """
        <div class="title-container">
            <img src="https://www.jewellerybox.co.uk/jb-shop-theme/images/general/jbAndroid-icon-192x192.png">
            <h1 class="nixie-font">jewellerybox custom apps</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("This is a handy launcher for various apps to make your life easier when working with data and at jewellerybox")

    st.divider()
    st.write("")

    # Define your other Streamlit apps, their URLs, and descriptions
    apps = {
        "Image Extractor": {
            "url": "https://jewellerybox-image-crawler.streamlit.app/",
            "description": "This app takes a list of product ids and tells you exactly which product images show up on each page",
            "icon": ":camera:"
        },
        "White Background Checker": {
            "url": "https://image-checker.streamlit.app/",
            "description": "This app takes a list of image URLs (from anywhere) and tells you if they have white backgrounds",
             "icon": ":art:"
        }

        # Add more apps as needed
    }

    for app_name, app_details in apps.items():
        # Using Markdown to display the icon with the app name
        st.markdown(f"### {app_details['icon']} {app_name}")

        st.write(app_details["description"])

        # Create a button for each app
        if st.button(f"Launch {app_name}"):
            webbrowser.open(app_details["url"], new=2)  # new=2 opens in a new tab

        # Add a separator line and space
        st.divider()
        st.write(" ")


if __name__ == "__main__":
    main()
