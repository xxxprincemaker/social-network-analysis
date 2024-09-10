---

# Analysis of Influence and Toxicity in Reddit's Social Network

This project investigates the dynamics of influence and toxicity within Reddit communities using the Reddit Hyperlink Network dataset. The analysis is conducted through computational methods and social network analysis algorithms to identify the most influential and toxic communities, and deduce their predominant themes.

## Objective

The main goal of this study is to identify the most influential and toxic subcommunities on Reddit and explore how influence and toxicity manifest in online social interactions.

## Project Description

This project uses a directed graph to model Reddit's social network, where each node represents a subcommunity (subreddit) and each edge represents a post containing a link to another subcommunity. The edges are weighted based on the sentiment of the posts (positive, neutral, or negative).

### Main Features

- **Influence Analysis:** Measured by the number of edges pointing to a community, using metrics such as degree centrality, authority, and PageRank.
- **Toxicity Analysis:** Measured by the number of edges with negative weights (negative interactions), indicating the toxicity of a community.
- **Detection of Predominant Communities:** Identification of communities based on influence and toxicity and deduction of predominant themes.

## Data Structure

The data used is from the [Reddit Hyperlink Network](https://snap.stanford.edu/data/soc-RedditHyperlinks.html) which includes:

- **SOURCE_SUBREDDIT and TARGET_SUBREDDIT:** Source and target communities.
- **POST_ID:** Identifier of the post.
- **TIMESTAMP:** Date and time of the post.
- **POST_LABEL:** Value -1 for negative posts and 1 for neutral or positive posts.
- **POST_PROPERTIES:** A 29-dimension vector representing textual properties of the posts.

## Requirements

- Python 3.x
- Libraries: `igraph`, `numpy`, `matplotlib`, `pandas`, `csv`, `cairo`, `PIL`.

## How to Use

1. **Install Dependencies:**
   ```bash
   pip install igraph numpy matplotlib pandas cairo pillow
   ```
2. **Run the Script:**
   - Place the `Reddit_Hyperlinks_-_Processado.tsv` file in the same directory as the script.
   - Run the script with `python analyze_reddit.py`.
   - Results will be displayed in the terminal, including the most influential and toxic subcommunities.

## Results

### Top 10 Most Influential Subcommunities

The script identifies subcommunities with the highest degree centrality, authority score, and PageRank score. Influential subcommunities like `askreddit` and `iama` stand out by attracting many interactions.

### Top 10 Most Toxic Subcommunities

Identified by negative interactions, communities such as `subredditdrama` and `circlebroke` were highlighted as the most toxic.

## Conclusion

This study reveals important insights into the dynamics of influence and toxicity on Reddit, contributing to a better understanding of online social interactions and helping to develop more effective moderation strategies.

## References

- Soares, L. F. A., Ferraz, Y. G., Castro, F., & Bevilaqua, H. (2023). Mapping the Terrain: Revealing Influence and Toxicity in Reddit's Social Network. Institute of Computing – UFRJ.
