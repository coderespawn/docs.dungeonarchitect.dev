document.addEventListener('DOMContentLoaded', function() {
    var checkExist = setInterval(function() {
        var divider = document.querySelector('.wh-header__divider');
        if (divider) {
            clearInterval(checkExist);

            // Create a container for the switch engine section
            var switchContainer = document.createElement('div');
            switchContainer.style.textAlign = 'right'; // Right align the content
            switchContainer.style.paddingRight = '20px'; // Right padding

            // Create the "Switch Engine:" text
            var switchText = document.createElement('span');
            switchText.textContent = 'Switch Engine:';
            switchText.style.marginRight = '10px'; // Spacing

            // Create the Unreal text (not a link)
            var unrealLink = document.createElement('a');
            unrealLink.href = '/unreal';
            unrealLink.textContent = 'Unreal';
            unrealLink.style.fontSize = '1em'; // Bigger font size
            unrealLink.style.color = 'grey'; // Grey color
            unrealLink.style.marginRight = '10px'; // Spacing

            // Create the Unity link
            var unityLink = document.createElement('a');
            unityLink.href = '/unity';
            unityLink.textContent = 'Unity';
            unityLink.style.fontSize = '1em'; // Smaller font size
            unityLink.style.color = 'grey'; // Grey color

            // Append elements to the container
            switchContainer.appendChild(switchText);
            switchContainer.appendChild(unrealLink);
            switchContainer.appendChild(unityLink);

            // Append the container to the divider
            divider.appendChild(switchContainer);
        }
    }, 100);
});
