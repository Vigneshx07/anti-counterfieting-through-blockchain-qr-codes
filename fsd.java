import javax.sql.DataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class RecordDao {

    private DataSource dataSource;
    private JdbcTemplate jdbcTemplate;

    public void setDataSource(DataSource dataSource) {
        this.dataSource = dataSource;
        this.jdbcTemplate = new JdbcTemplate(dataSource);
    }

    public void insertRecord(Record record) {
        String sql = "INSERT INTO records (id, name, age) VALUES (?, ?, ?)";
        Object[] params = { record.getId(), record.getName(), record.getAge() };
        jdbcTemplate.update(sql, params);
    }
}
