# custom-classification-algorithm
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
    <p>Although we cannot say for certain whether something comes from a data set without actually knowing, using this method we can get pretty good at guessing. Using a t-test, we can get the probability of a sample being drawn from a distribution. This is got be getting the area under the curve from our data point to the closest tail of the distribution. After this calculus wizardy is performed, we are left with the probability or p-value.</p>
    <h2>The Algorithim</h2>
    <p>If we are trying to classify data points into a category, we can look at the normal distributions and see which one would be more likely to contain a certain element. Let's say we are given someones 1 rep maximum bench press in pounds, and we want to predict their profession.
        For some reason assume we have a data set of data scientists and police officers max bench. If we have someone named Charlie who's max bench is 85lbs, do you think they are a data scientist or police officer? 
    </p>
    <a href="https://ibb.co/KFNhJkJ"><img src="https://i.ibb.co/72gCq5q/bench.png" alt="bench" border="0"></a>
    <p>Judging by the graph, we can predict with reasonably accuracy that Charlie knows a lot more about Excel than traffic laws. </p>