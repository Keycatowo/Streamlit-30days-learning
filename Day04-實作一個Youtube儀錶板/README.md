# Day04-範例參考：實作一個Youtube Dashboard


## 重點


## 執行
```sh
streamlit run Ken_Dashboard.py
```


## 嘗試與問題
目前嘗試執行發現有錯誤無法執行，之後再回來看問題在哪裡
```python
InvalidIndexError: Reindexing only valid with uniquely valued Index objects

File "C:\_Code\Miniconda\envs\data38\lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 564, in _run_script
    exec(code, module.__dict__)
File "A:\_Data\Code\Pratice【個人練習】\【套件練習】\Streamlit-30days-learning\Day04-實作一個Youtube儀錶板\Ken_Dashboard.py", line 83, in <module>
    views_days = pd.pivot_table(df_time_diff_yr,index= 'days_published',values ='Views', aggfunc = [np.mean,np.median,lambda x: np.percentile(x, 80),lambda x: np.percentile(x, 20)]).reset_index()
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\pivot.py", line 92, in pivot_table
    table = concat(pieces, keys=keys, axis=1)
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\concat.py", line 294, in concat
    op = _Concatenator(
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\concat.py", line 479, in __init__
    self.new_axes = self._get_new_axes()
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\concat.py", line 549, in _get_new_axes
    return [
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\concat.py", line 550, in <listcomp>
    self._get_concat_axis if i == self.bm_axis else self._get_comb_axis(i)
File "pandas\_libs\properties.pyx", line 37, in pandas._libs.properties.CachedProperty.__get__
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\concat.py", line 607, in _get_concat_axis
    concat_axis = _make_concat_multiindex(
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\reshape\concat.py", line 709, in _make_concat_multiindex
    mapped = level.get_indexer(hlevel)
File "C:\_Code\Miniconda\envs\data38\lib\site-packages\pandas\core\indexes\base.py", line 3442, in get_indexer
    raise InvalidIndexError(self._requires_unique_msg)

```

## 延伸閱讀
+ [線上版本範例](https://playingnumbers-yt-dashboard-st-ken-dashboard-d3hqi6.streamlit.app/)