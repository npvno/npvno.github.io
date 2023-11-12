// Load and parse the JSON data
fetch('top_posts.json')
    .then(response => response.json())
    .then(data => {
        const postTables = document.getElementById('post-tables');

        // Iterate through the users and create HTML elements
        for (let i = 0; i < data.posts.length; i += 3) {
            // Create a new table for each row
            const postTable = document.createElement('table');
            postTable.style.width = '100%';

            // Create a new table row for each group of three posts
            const postTableRow = document.createElement('tr');

            for (let j = i; j < i + 3 && j < data.posts.length; j++) {
                // Create a new table cell for each post
                const postTableCell = document.createElement('td');

                // Create a span element to contain "Post ID:" and ${post}
                const postTextSpan = document.createElement('span');
                postTextSpan.style.display = 'inline'; // Set display to inline
                postTextSpan.textContent = 'Post ID: ';

                // Create an anchor element for the clickable ${post}
                const postLink = document.createElement('a');
                postLink.href = `https://www.instagram.com/p/${data.posts[j]}`;
                postLink.target = '_blank';
                postLink.textContent = `${data.posts[j]}`;

                // Create the blockquote element
                const blockquote = document.createElement('blockquote');
                blockquote.setAttribute('style', 'width: 300px;');
                blockquote.setAttribute('class', 'instagram-media');
                blockquote.setAttribute('data-instgrm-version', '14');
                blockquote.setAttribute('omitscript', 'true');

                const blockquoteLink = document.createElement('a');
                blockquoteLink.href = `https://www.instagram.com/p/${data.posts[j]}/`;
                blockquote.appendChild(blockquoteLink);

                // Append the postLink and blockquote to the postTableCell
                postTextSpan.appendChild(postLink);
                postTableCell.appendChild(postTextSpan);
                postTableCell.appendChild(blockquote); // Append the blockquote element

                // Append the postTableCell to the postTableRow
                postTableRow.appendChild(postTableCell);
            }

            // Append the postTableRow to the postTable
            postTable.appendChild(postTableRow);

            // Append the postTable to the postTables
            postTables.appendChild(postTable);
        }
    })
    .catch(error => {
        console.error('Error loading JSON data:', error);
    });

