% include("./templates/search.tpl")
<br><br>
<h2>Search Results for '{{query}}'</h2>
<ul class="search-results">
% for r in results:
% if 'episodeid' in r:
<li class="search-result" onclick="Browse.loadEpisode('{{r['showid']}}', '{{r['episodeid']}}')">{{r['text']}}</li>
<br/>
% else:
<li class="search-result" onclick="Browse.loadShow('{{r['showid']}}')">{{r['text']}}</li>
<br/>
% end
% end
% if not results:
    No Results :(
% end

</ul>