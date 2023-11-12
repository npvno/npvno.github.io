
// Load and parse the JSON data
fetch('top_posts.json')
    .then(response => response.json())
    .then(data => {
        const postTables = document.getElementById('post-tables');

        // Iterate through the users and create HTML elements
        data.posts.forEach(post => {
            
            const postTable = document.createElement('table');
            postTable.style.width = '100%';
            const postTableRow = document.createElement('tr');

            
            const postTableCell = document.createElement('td');

            // Create a span element to contain "Post ID:" and ${post}
            const postTextSpan = document.createElement('span');
            postTextSpan.style.display = 'inline'; // Set display to inline
            postTextSpan.textContent = 'Post ID: ';

            // Create an anchor element for the clickable ${post}
            const postLink = document.createElement('a');
            postLink.href = `https://www.instagram.com/p/${post}`;
            postLink.target = '_blank';
            postLink.textContent = `${post}`;

            // Create the blockquote element
            const blockquote = document.createElement('blockquote');
            blockquote.setAttribute('style', 'width: 300px;');
            blockquote.setAttribute('class', 'instagram-media');
            blockquote.setAttribute('data-instgrm-version', '14');
            blockquote.setAttribute('omitscript', 'true');

            const blockquoteLink = document.createElement('a');
            blockquoteLink.href = `https://www.instagram.com/p/${post}/`;
            blockquote.appendChild(blockquoteLink);

            // Append the postLink and blockquote to the postTableCell
            postTextSpan.appendChild(postLink);
            postTableCell.appendChild(postTextSpan);
            postTableCell.appendChild(blockquote); // Append the blockquote element
            postTableRow.appendChild(postTableCell); 
            

            postTables.appendChild(postTableRow);
        });
    })

    .catch(error => {
        console.error('Error loading JSON data:', error);
    });

