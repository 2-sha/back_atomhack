from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=255)
    parent = models.ForeignKey('self', verbose_name='Родительский департамент', on_delete=models.CASCADE,
                               related_name='children', null=True, blank=True, default=None)

    @property
    def workload(self):
        workload_sum = 0
        n = 0
        for user in self.users.all():
            n += 1
            workload_sum += user.workload
        return round(workload_sum / n, 2)

    @property
    def kpi(self):
        kpi_sum = 0
        n = 0
        for user in self.users.all():
            n += 1
            kpi_sum += user.kpi
        return round(kpi_sum / n, 2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'департамент'
        verbose_name_plural = 'департаменты'
