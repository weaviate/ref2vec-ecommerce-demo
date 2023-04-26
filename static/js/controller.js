document.addEventListener("DOMContentLoaded", function() {

    const imageCells = document.querySelectorAll(".image-cell");
    imageCells.forEach(cell => {
        const image = cell.querySelector("img");
        const imagePath = image.getAttribute("id");
        const clickListener = createClickListener(image);
        image.addEventListener("click", clickListener);
        image.listener = clickListener;
    });

    const searchBar = document.querySelector(".search-bar");
    searchBar.addEventListener("keydown", function(event) {
        if (event.keyCode === 13 || event.which === 13) {
          handleSearchInput(event);
        }
    });

    // todo, refactor these click handler functions to separate files
    function handleImageClick(data) {
        console.log(data);
        fetch("/image-clicked", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ imagePath: data })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
              }
              return response.json();
        })
        .then(data => {
            // Handle the response from the Python controller
            // Update the image elements on the page with the new image paths
            const imageCells = document.querySelectorAll(".image-cell");
            console.log(data);
            const newData = data["data"];
            //const image_dict = data["image_dict"];
            const userClicks = new Set(data["user_clicks"]);
            imageCells.forEach((cell, index) => {
                const image = cell.querySelector("img");
                //const imagePath = data.image_dict["image"+String(index)];
                const imagePath = newData[index]["image_path"];
                const distance = newData[index]["distance"];
                image.src = "/static/" + imagePath;
                image.id = imagePath;
    
                // Update the h2 element with the new image path
                const h2Element = cell.querySelector("h2");
                h2Element.textContent = "Distance to centroid: " + distance;
    
                console.log(userClicks.has(image.id));
                if (userClicks.has(image.id)) {
                    image.classList.add("clicked-image");
                } else {
                    image.classList.remove("clicked-image")
                }
                
                const oldClickListener = image.listener; // Retrieve the reference to the old listener
                image.removeEventListener("click", oldClickListener);
                const newClickListener = createClickListener(image);
                image.addEventListener("click", newClickListener);
                image.listener = newClickListener; // Store the reference to the new listener
            });
        })
        .catch(error => {
            console.error(error);
        });
    
    }

    function createClickListener(image) {
        return function() {
            handleImageClick(image.id);
        }
    }

    // Function to handle the search input event
    function handleSearchInput(event) {
        // Get the search query entered by the user
        const searchQuery = event.target.value;

        // Call the function to handle the search query
        handleSearch(searchQuery);
    }

    function handleSearch(searchQuery) {
        // Here, you can process the search query as needed
        console.log(searchQuery);

        // Example: Send search query to the server using Fetch API
        fetch("/text-search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ searchQuery: searchQuery })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            // Handle the response from the Python controller
            // Update the image elements on the page with the new image paths
            const imageCells = document.querySelectorAll(".image-cell");
            const newData = data["data"];
            const userClicks = new Set(data["user_clicks"]);
            imageCells.forEach((cell, index) => {
                const image = cell.querySelector("img");
                const imagePath = newData[index]["image_path"];
                const distance = newData[index]["distance"];
                image.src = "/static/" + imagePath;
                image.id = imagePath;
    
                // Update the h2 element with the new image path
                const h2Element = cell.querySelector("h2");
                h2Element.textContent = "Distance to centroid: " + distance;
    
                if (userClicks.has(image.id)) {
                    image.classList.add("clicked-image");
                } else {
                    image.classList.remove("clicked-image")
                }
                
                const oldClickListener = image.listener; // Retrieve the reference to the old listener
                image.removeEventListener("click", oldClickListener);
                const newClickListener = createClickListener(image);
                image.addEventListener("click", newClickListener);
                image.listener = newClickListener; // Store the reference to the new listener
            });
            
            const searchBar = document.querySelector(".search-bar");
            searchBar.innerHTML = "";
            //clear out the text in the searchbar as well
        })
        .catch(error => {
            console.error(error);
        });
    }
});