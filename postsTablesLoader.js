
// Load and parse the JSON data
fetch('data.json')
    .then(response => response.json())
    .then(data => {
        const postTables = document.getElementById('post-tables');

        // Iterate through the users and create HTML elements
        data.users.forEach(user => {
            const userDiv = document.createElement('div');
            const usernameH2 = document.createElement('h2')
            const usernameLink = document.createElement('a');
            usernameLink.href = `https://www.instagram.com/${user.username}`;
            usernameLink.target = '_blank';
            usernameLink.textContent = user.username;
            usernameH2.appendChild(usernameLink);
            userDiv.appendChild(usernameH2);

            
            const postTable = document.createElement('table');
            postTable.style.width = '100%';
            const postTableRow = document.createElement('tr');

            user.postIDs.forEach(postID => {
                const postTableCell = document.createElement('td');

                // Create a span element to contain "Post ID:" and ${postID}
                const postTextSpan = document.createElement('span');
                postTextSpan.style.display = 'inline'; // Set display to inline
                postTextSpan.textContent = 'Post ID: ';

                // Create an anchor element for the clickable ${postID}
                const postLink = document.createElement('a');
                postLink.href = `https://www.instagram.com/p/${postID}`;
                postLink.target = '_blank';
                postLink.textContent = `${postID}`;


                // Create the blockquote element
                const blockquote = document.createElement('blockquote');
                blockquote.setAttribute('style', 'width: 300px;');
                blockquote.setAttribute('class', 'instagram-media');
                blockquote.setAttribute('data-instgrm-version', '14');
                blockquote.setAttribute('omitscript', 'true');

                const blockquoteLink = document.createElement('a');
                blockquoteLink.href = `https://www.instagram.com/p/${postID}/`;
                blockquote.appendChild(blockquoteLink);

                // Append the postLink and blockquote to the postTableCell
                postTextSpan.appendChild(postLink);
                postTableCell.appendChild(postTextSpan);
                postTableCell.appendChild(blockquote); // Append the blockquote element
                postTableRow.appendChild(postTableCell); 
            });

          postTable.appendChild(postTableRow);
          userDiv.appendChild(postTable);
          userDiv.appendChild(document.createElement('hr'));
          postTables.appendChild(userDiv);
        });
    })

    .catch(error => {
        console.error('Error loading JSON data:', error);
    });

