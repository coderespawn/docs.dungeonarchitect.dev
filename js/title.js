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
            var unrealText = document.createElement('span');
            unrealText.textContent = 'Unreal';
            unrealText.style.fontSize = '1.2em'; // Bigger font size
            unrealText.style.marginRight = '10px'; // Spacing

            // Create the Unity link
            var unityLink = document.createElement('a');
            unityLink.href = '/unity';
            unityLink.textContent = 'Unity';
            unityLink.style.fontSize = '1em'; // Smaller font size
            unityLink.style.color = 'grey'; // Grey color

            // Append elements to the container
            switchContainer.appendChild(switchText);
            switchContainer.appendChild(unrealText);
            switchContainer.appendChild(unityLink);

            // Append the container to the divider
            divider.appendChild(switchContainer);
        }
    }, 100);
});
