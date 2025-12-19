SUMMARY
This repository contains SQL analytics projects focused on analyzing user behavior and marketing performance using a structured dataset generated with Python. The dataset simulates real-world product and marketing scenarios, including user signups and geographic distribution, daily user activity, marketing campaigns, and campaign impressions and clicks. All data is provided as CSV files and SQL seed scripts to ensure transparency, reproducibility, and clarity around the analytical assumptions used in the project.


QUESTIONS ANSWERED
The following are the questions that are answered in the project:
- How many daily active users does the product have?
- How is the user base distributed by country?
- Which marketing campaigns drive the most engagement?


DATA ANALYSIS
The results of the project are as follows:

User engagement tracking
-Daily active users fluctuates between 13 and 28 users, indicating moderate but consistent engagement
-February 4th shows a clear peak (28 users), significantly above the average
-Engagement remains relatively stable after the peak, suggesting no sharp churn

Geographic insights
-Australia and the US represent the largest portions of the user base
-User distribution is relatively balanced across regions
-India has the smallest user count, indicating potential growth opportunity

Campaign performance evaluation
-Holiday Discount significantly outperforms other campaigns
-Performance drops gradually across the remaining campaigns
-Promotional and incentive-based campaigns outperform awareness-focused efforts



POTENTIAL BUSINESS IMPACT
The analyses in this repository support common decision-making scenarios in product and marketing teams:

User engagement tracking
-Daily active user metrics help identify usage trends, measure product adoption, and detect changes in user behavior over time.

Geographic insights
-Understanding user distribution by country informs localization strategy, regional marketing spend, and infrastructure planning.
-Balanced distribution reduces over-reliance on a single market

Campaign performance evaluation
-Campaign performance data helps optimize marketing spend and messaging
-Ranking campaigns by clicks and impressions highlights which initiatives generate the most engagement and which underperform.This information can be used to determine which campaigns to scale.

These insights enable teams to prioritize high-impact initiatives, allocate resources more effectively, and monitor performance using clear, repeatable metrics.



RECCOMENDATIONS
Based on the types of analyses performed, typical next steps for a business would include:

- Scale high-performing campaigns 
  Increase investment in campaigns that consistently rank high in engagement metrics and test similar messaging or channels.

- Optimize underperforming regions
  For countries with lower activity or adoption, investigate onboarding flows, pricing, or localization opportunities.

- Monitor engagement trends over time 
  Track daily active users alongside campaign launches or product changes to understand causal impact.

- Expand analysis with joins and funnels  
  Connecting user activity with campaign exposure can reveal conversion rates and drop-off points, enabling more targeted optimization.


