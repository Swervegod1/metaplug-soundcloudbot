# SoundcloudScraper
Scrape Soundcloud for artists info (managers, followers, etc)

How To Use:
1.  main.py -i \<iterations\> -f \<follower_min\> -s \<start_artist\>

    iterations (default 10): number of users to recurse. each user will give about 50 more users
        
    follower_min (default 10000): minimum number of followers to be accepted
    
    start_artist (default alex_shortt): artist to begin looking at followers (also reverts back to this artist if user has no followings)
    
2. copy results from add_to_catalogue.xlsx to bottom of catalogue.xlsx
3. delete add_to_catalogue.xlsx
4. restart!