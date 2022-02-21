# f - файл, [l, r] - рассматриваемый отрезок, на котором ищем оптималный

def best(f, l, r):
  s = f'samtools view {f} chr11:{l}-{r} | cut -f1 | sort -u | wc -l'
  !$s
