# custom-classification-algorithm

<body>
    <h1> Classification Algorithim </h1>
    <h2>Purpose: Classify Categorical Data using Normally Distributed Factors</h2>
    <h3>Background: What is a p-value?</h3>
    <p>As you may be aware, data tends to follow a normal distribution. This allows us to make statements about/with the data. One of the ways we can do this is with probability.</p>
    <a href="https://ibb.co/k1NPDY3"><img src="https://i.ibb.co/pyYkKCW/Screenshot-at-May-02-14-01-03.png" alt="Screenshot-at-May-02-14-01-03" border="0"></a>
    <p>If we have a set of data, we can generate one of these curves. Due to the central limit theorem, we can make statements about a data point's likelihood of belonging to a set. For instance, the blue dot is a lot closer to the mean than the green dot. We can use statistics and 
        probability to make a statement about "the likelihood of a sample this or more extreme being drawn from our distribution". This is a powerful statement, but it has a few limitations:
    </p>
    <ul>
        <li>This statement is only about drawing from our distribution, it does not mean definitively that it has a certain probability of coming from the data set. </li>
        <li>We can only be as confident with this statement as we are that our sample is reflective of the population.</li>
    </ul>
    <p>Although we cannot say for certain whether something comes from a data set without actually knowing, using this method we can get pretty good at guessing. Using a t-test, we can get the probability of a sample being drawn from a distribution. This is got be taking the area under the curve from our data point to the closest tail of the distribution. After this calculus wizardy is performed, we are left with the probability or p-value.</p>
    <h2>The Algorithim</h2>
    <p>If we are trying to classify data points into a category, we can look at the normal distributions and see which one would be more likely to contain a certain element. Let's say we are given someones 1 rep maximum bench press in pounds, and we want to predict their profession.
        For some reason assume we have a data set of data scientists and police officers max bench. If we have someone named Charlie who's max bench is 85lbs, do you think they are a data scientist or police officer? 
    </p>
    <a href="https://ibb.co/KFNhJkJ"><img src="https://i.ibb.co/72gCq5q/bench.png" alt="bench" border="0"></a>
    <p>Judging by the graph, we can predict with reasonably accuracy that Charlie knows a lot more about Excel than traffic laws. </p>
    <p>What if we add a third career in there? Say highschool gym teachers. Now we want to figure out Carlos' job.</p>
    <a href="https://ibb.co/tBrgKMf"><img src="https://i.ibb.co/qBQKjMG/gymbench.png" alt="gymbench" border="0"></a>
    <p>This creates an interesting problem, as using this metric any yolked gym teacher (yolked gym teacher meaning can bench 150 or more) will be incorrectly classified as a police officer. The solution?
        Look at other dimensions of course! Here, we have the time it took people to run 2 kilometers, with Carlos in there as well.</p>
        <a href="https://ibb.co/306GV9n"><img src="https://i.ibb.co/y8vGKcr/runtimes.png" alt="runtimes" border="0"></a>
        <p>Now, I hear you saying "How does this change anything? We still have the same overlap as before!" And this is true. However, if we multiply the p-values together, we will get a more broad picture. If the p-values for Carlos are as follows: </p>
        <ul>
            <li>Data Scientist - Bench Press : 0.000000, Running : 0.98</li>
            <li>Police Officer - Bench Press : 0.401, Running : 0.89</li>
            <li>Gym Teacher - Bench Press : 0.96, Running : 0.06</li>
        </ul>
        <p>We can multiply the p-values togeher. When something is extremely improbable, (Carlos being a Data Scientist based on his bench) the dot-product (result of multiplying all items in a list) will go to 0. This gives us a well rounded estimate as to Carlos' true profession, allowing us to look at multiple factors.
            This is the algorithim for classification I have written. 
        </p>
        <h2>Adam's Super Duper Cool Python Implementation</h2>
        <p>The way I went about testing this algorithim was using the Iris data set.</p>
        <a href="https://archive.ics.uci.edu/ml/datasets/iris">Iris Dataset available here.</a>
        <p>I used a a pandas data frame to import the data, and created bell curves using 80% of the data for each numeric factor. I then ran t-tests on the other 20% of the data in each distribution. I used a bash script to repeat the test 100 times. The result is an average accuracy of 94.47 correct classification.
            If the data set were larger, the distribution of accuracies would appear continuous. However, since there are 149 items in the Iris dataset, the results appear discrete. The following graph shows the distribution of accuracies.
        </p>
        <a href="https://ibb.co/LRk0V1d"><img src="https://i.ibb.co/PjmrqgG/test-results.png" alt="test-results" border="0"></a>
        <p>Each bar represents the number of wrong guesses in addition to the accuracy. 100 is 0, 96.7 1, and so forth.</p>
        <p>The only confound that I can think of is with how the testing data is selected. I chose 20% of the data to be testing based on random indices (0-148) as opposed to each group being 20% (so 20% of setosa, virginica, versiocolor). This could possibly be more accurate. As well, doing analysis on the accuracy for each factor as opposed to the whole could give a better picture as well.</p>

</body>
